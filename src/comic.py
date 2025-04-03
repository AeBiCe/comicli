from pathlib import Path
import zipfile
import typer
import exceptions, directories
from pydantic import BaseModel

app = typer.Typer(no_args_is_help=True)


@app.command()
def create(directory: Path, save_location: Path = Path(".")):
    print(f"Creating a comic archive of {directory.name}")
    if not validate(directory):
        raise exceptions.ValidationError(f"Error validating {directory}")
    with zipfile.ZipFile(f"{save_location}/{directory.name}.cbz", mode="w") as comic:
        for file in directory.iterdir():
            comic.write(file, arcname=file.name)


def validate(path: Path):
    """Perform various validation tests"""
    return _validate_file_extensions(path) and _validate_file_order(path)


def _validate_file_extensions(path: Path) -> bool:
    """Validate that the directory only contains images"""
    for file in directories.get_files(path=path):
        if file.suffix.lower() not in {".jpg", ".jpeg", ".png"}:
            return False
    return True


def _validate_file_order(path: Path):
    """Validate that no page (number) is missing"""
    files = directories.get_file_names(path=path, with_extension=False)
    files = [int(file) for file in files]  # Assuming filenames are 1.png, 2.png..
    files.sort()

    for file in range(min(files), max(files)):
        if file + 1 not in files:
            print(f"{file+1} was not found in {path}")
            return False
    return True


def _validate_no_duplicates(path: Path):
    """Validate that there are no dupllicate files"""
    pass


class Comic(BaseModel):
    path: Path
    title: str
    issue: int
    pages: int
    publisher: str
