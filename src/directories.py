from pathlib import Path


def get_dirs(path: Path) -> list[Path]:
    return [x.absolute() for x in path.iterdir() if x.is_dir()]


def get_files(path: Path) -> list[Path]:
    return [x.absolute() for x in path.iterdir() if x.is_file()]


def dir_contains_only_images(path: Path) -> bool:
    for file in path.iterdir():
        return file.is_file() and file.suffix.lower() in {".jpg", ".jpeg", ".png"}
    return False
