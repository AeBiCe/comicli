import typer
from typing_extensions import Annotated

import directories
from pathlib import Path

from rich import print  # This will be centralized later

app = typer.Typer(no_args_is_help=True)

""" TODO:
Learn how to make the scan function default when running the app to avoid
$ comicli scan scan
"""


@app.command()
def scan(path: Annotated[str, typer.Argument()] = "."):
    dirs = directories.get_dirs(Path(path))
    for dir in dirs:
        if directories.dir_contains_only_images(dir):
            print(f"{dir.name} is comic material :party_popper:")
    print("Done searching!")
