import typer

import comic
import scanner
import constants
from rich import print

app = typer.Typer(no_args_is_help=True)
app.add_typer(comic.app, name="comic")
app.add_typer(scanner.app, name="scan")


@app.command()
def logo():
    print(constants.LOGO)


if __name__ == "__main__":
    app()
