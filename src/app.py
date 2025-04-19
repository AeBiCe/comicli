from pathlib import Path

import typer
from rich import print
from rich.tree import Tree
from typing_extensions import Annotated

import constants
from directories import directories
import comic

app = typer.Typer(no_args_is_help=True)
app.add_typer(comic.app, name="comic")


@app.command()
def logo():
    print(constants.LOGO)


@app.command()
def scan(
    path: Annotated[Path, typer.Argument()] = Path("."),
):
    directory = Path(path).absolute()

    comics = directories.find_comic_dirs(directory)

    tree = Tree(str(path))
    for comic in comics:
        tree.add(str(comic.relative_to(directory)))

    print("These directories can be converted to comics:", tree)


if __name__ == "__main__":
    app()
