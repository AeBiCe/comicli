import typer

import directories
import constants

app = typer.Typer(no_args_is_help=True)


@app.command()
def logo():
    print(constants.LOGO)


@app.command()
def scan():
    dirs = directories.get_dirs()
    for dir in dirs:
        if directories.dir_contains_only_images(dir):
            print(f"{dir.name} is able to become a comic :party_popper:")
    print("Done searching!")


if __name__ == "__main__":
    app()
