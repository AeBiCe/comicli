from pydantic.dataclasses import dataclass
from pathlib import Path


@dataclass
class Comic:
    name: str
    pages: int
    directory: Path

    @classmethod
    def from_path(cls):
        pass

    @classmethod
    def from_dict(cls):
        pass

    @classmethod
    def create(cls):
        pass
