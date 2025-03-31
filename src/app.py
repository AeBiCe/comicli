import typer
from typing_extensions import Annotated

import directories
import constants
from pathlib import Path
from rich import print

app = typer.Typer(no_args_is_help=True)


@app.command()
def logo():
    print(constants.LOGO)


@app.command()
def scan(path: Annotated[str, typer.Argument()] = "."):
    dirs = directories.get_dirs(Path(path))
    for dir in dirs:
        if directories.dir_contains_only_images(dir):
            print(f"{dir.name} is comic material :party_popper:")
    print("Done searching!")


if __name__ == "__main__":
    app()
