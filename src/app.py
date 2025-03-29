import typer

import directories
import constants

from rich import print


app = typer.Typer(no_args_is_help=True)


@app.command()
def logo():
    print(constants.LOGO)


@app.command()
def scan():
    print(directories.scan())


if __name__ == "__main__":
    app()
