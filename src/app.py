import typer
from typing_extensions import Annotated

from pathlib import Path
import comic, constants, directories
from rich import print

app = typer.Typer(no_args_is_help=True)
app.add_typer(comic.app, name="comic")


@app.command()
def logo():
    print(constants.LOGO)


@app.command()
def scan(path: Annotated[str, typer.Argument()] = "."):
    directory = Path(path).absolute()
    dirs = [
        dir for dir in directories.get_dirs(directory) if len(list(dir.iterdir())) > 0
    ]

    print(f"Checking {directory}..")

    for dir in dirs:
        if directories.dir_contains_only_images(dir):
            print(f"{dir.name} is comic material :book:")


if __name__ == "__main__":
    app()
