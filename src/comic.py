from pathlib import Path
import zipfile
import typer
import re
import exceptions, directories
from pydantic import BaseModel
from typing_extensions import Annotated
from rich import print

app = typer.Typer(no_args_is_help=True)


@app.command()
def create(
    directory: Annotated[Path, typer.Argument()],
    save_location: Annotated[Path, typer.Argument()] = Path("."),
    dry_run: Annotated[bool, typer.Option("--dry", "-d")] = False,
):
    try:
        validate(directory)
    except exceptions.ValidationError as err:
        print(f":collision: Failed to validate the path :collision: \n{err}")
        raise typer.Exit(code=1)
    if dry_run:
        print(f"Would create {save_location}/{directory.name}.cbz")
        return
    with zipfile.ZipFile(f"{save_location}/{directory.name}.cbz", mode="w") as comic:
        print(f"Creating a comic archive of {directory.name}")
        for file in directory.iterdir():
            comic.write(file, arcname=file.name)


def validate(path: Path):
    """Perform various validation tests"""
    _validate_is_dir(path)
    _validate_file_extensions(path)
    _validate_file_order(path)


def _validate_is_dir(path: Path):
    if not path.is_dir():
        raise exceptions.ValidationError("Path is not a directory")


def _validate_file_extensions(path: Path):
    """Validate that the directory only contains images"""
    for file in directories.get_files(path=path):
        if file.suffix.lower() not in {".jpg", ".jpeg", ".png"}:
            raise exceptions.ValidationError(f"{file.name} is not an image")


def _get_page_from_name(filename: str):
    return int(re.findall(r"\d+", filename)[-1])


def get_pages(path: Path):
    files = directories.get_file_names(path=path, with_extension=False)
    files = [_get_page_from_name(file) for file in files]
    files.sort()
    return files


def find_missing_pages(path: Path) -> list[int]:
    pages = get_pages(path)
    return [page not in range(pages[-1]) for page in pages]


def _validate_file_order(path: Path):
    """Validate that no page (number) is missing"""
    files = directories.get_file_names(path=path, with_extension=False)
    files = [_get_page_from_name(file) for file in files]
    files.sort()

    for file in range(min(files), max(files)):
        if file + 1 not in files:
            print(f"{file+1} was not found in {path}")
            return False
    return True


def _validate_no_duplicates(path: Path):
    """Validate that there are no dupllicate files"""
    pass
