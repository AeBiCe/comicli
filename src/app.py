import typer
import pathlib


def main(name: str):
    """Test application that greets people

    Args:
        name (str): The person to greet
    """
    print(f"Hello {name}!")


if __name__ == "__main__":
    typer.run(main)
