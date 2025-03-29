from pathlib import Path


def scan():
    p = Path(".")
    return [x for x in p.iterdir() if x.is_dir()]
