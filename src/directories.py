from pathlib import Path

IMG_EXT = {".jpg", ".jpeg", ".png"}


def get_dirs(path: Path) -> list[Path]:
    return [x.absolute() for x in path.iterdir() if x.is_dir()]


def get_files(path: Path) -> list[Path]:
    return [x.absolute() for x in path.iterdir() if x.is_file()]


def get_file_names(path: Path, with_extension: bool = True) -> list[str]:
    return [x.name if with_extension else x.stem for x in get_files(path)]


def get_file_extensions(path: Path) -> set[str]:
    return {x.suffix for x in get_files(path)}


def file_in_dir(filename: str, directory: Path) -> bool:
    return filename in get_file_names(directory, False)


def dir_contains_only_images(path: Path) -> bool:
    return all(x.suffix.lower() in IMG_EXT for x in get_files(path))
