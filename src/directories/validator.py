import re
from pathlib import Path

import typer

from exceptions import ValidationError
from collections import Counter
from rich import print

from . import directories


def validate(path: Path):
    """Perform various validation tests"""
    try:
        validate_is_dir(path)
        validate_file_extensions(path)
        validate_file_order(path)
        validate_no_duplicates(path)
    except ValidationError as err:
        print(f":collision: Validation error :collision: \n{err}")
        raise typer.Exit(code=1)


def validate_is_dir(path: Path):
    if not path.is_dir():
        raise ValidationError("Path is not a directory")


def validate_file_order(path: Path):
    """Validate that no page (number) is missing"""
    pages = _get_pages(path)

    missing_pages = [page for page in range(pages[0], pages[-1]) if page not in pages]

    if missing_pages:
        raise ValidationError(f"Missing page(s): {missing_pages}")


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


def validate_no_duplicates(path: Path):
    """Validate that there are no dupllicate files"""
    pages = _get_pages(path)

    if len(pages) > pages[-1]:
        duplicates = [item for item, count in Counter(pages).items() if count > 1]
        raise ValidationError(f"Duplicates Page(s): {duplicates}")
    pass
