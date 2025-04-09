import zipfile
from pathlib import Path

import typer
from rich import print
from typing_extensions import Annotated

from directories.validator import validate

app = typer.Typer(no_args_is_help=True)


@app.command()
def create(
    directory: Annotated[Path, typer.Argument()],
    save_location: Annotated[Path, typer.Argument()] = Path("."),
    dry_run: Annotated[bool, typer.Option("--dry", "-d")] = False,
):
    validate(directory)
    if dry_run:
        print(f"Would create {save_location}/{directory.name}.cbz")
        raise typer.Exit(code=0)
    with zipfile.ZipFile(f"{save_location}/{directory.name}.cbz", mode="w") as comic:
        print(f"Creating a comic archive of {directory.name}")
        for file in directory.iterdir():
            comic.write(file, arcname=file.name)
