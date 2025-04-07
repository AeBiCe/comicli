import re
from pathlib import Path

import typer

import directories
from exceptions import ValidationError


def validate(path: Path):
    """Perform various validation tests"""
    try:
        validate_is_dir(path)
        validate_file_extensions(path)
        validate_file_order(path)
    except ValidationError as err:
        print(f":collision: Validation error :collision: \n{err}")
        raise typer.Exit(code=1)


def validate_is_dir(path: Path):
    if not path.is_dir():
        raise ValidationError("Path is not a directory")


# WIP DOES NOT WORK AS OF NOW
def validate_file_order(path: Path):
    """Validate that no page (number) is missing"""
    pages = _get_pages(path)

    missing_pages = [page for page in pages if page not in range((pages[-1] + 1))]

    if missing_pages:
        raise ValidationError(f"Pages: {missing_pages} are missing")


def validate_file_extensions(path: Path):
    """Validate that the directory only contains images"""
    for file in directories.get_files(path=path):
        if file.suffix.lower() not in {".jpg", ".jpeg", ".png"}:
            raise ValidationError(f"{file.name} is not an image")


def _get_page_number_from_name(filename: str):
    return int(re.findall(r"\d+", filename)[-1])


def _get_pages(path: Path):
    files = directories.get_file_names(path=path, with_extension=False)
    files = [_get_page_number_from_name(file) for file in files]
    files.sort()
    return files


def _validate_no_duplicates(path: Path):
    """Validate that there are no dupllicate files"""
    pass
