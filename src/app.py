import typer
from typing_extensions import Annotated

from pathlib import Path
import comic, constants
from rich import print

app = typer.Typer(no_args_is_help=True)
app.add_typer(comic.app, name="comic")


@app.command()
def logo():
    print(constants.LOGO)


@app.command()
def scan(path: Annotated[str, typer.Argument()] = "."):
    pass


if __name__ == "__main__":
    app()
