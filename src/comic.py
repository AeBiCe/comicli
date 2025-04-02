from pathlib import Path
import zipfile
import typer

app = typer.Typer(no_args_is_help=True)


@app.command()
def create(directory: Path, save_location: Path = Path(".")):
    print(f"Creating a comic archive of {directory.name}")
    with zipfile.ZipFile(f"{save_location}/{directory.name}.cbz", mode="w") as comic:
        for file in directory.iterdir():
            comic.write(file, arcname=file.name)


def validate(path: Path):
    """Perform various validation tests"""
    pass


def _validate_file_extensions(path: Path) -> bool:
    """Validate that the directory only contains images"""
    for file in path.iterdir():
        return file.is_file() and file.suffix.lower() in {".jpg", ".jpeg", ".png"}
    return False


def _validate_file_order(path: Path):
    """Validate that no page (number) is missing"""
    files = [file.name for file in path.iterdir()]
    files.sort()
    pass


def _validate_no_duplicates(path: Path):
    """Validate that there are no dupllicate files"""
    pass
