from pathlib import Path


def get_dirs(path: Path) -> list[Path]:
    return [x.absolute() for x in path.iterdir() if x.is_dir()]


def get_files(path: Path) -> list[Path]:
    return [x.absolute() for x in path.iterdir() if x.is_file()]
