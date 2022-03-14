from pathlib import Path
from dataclasses import dataclass

from .utils import fromDict


@dataclass
class Signature:
    path: Path

    @classmethod
    def fromDict(cls, data):
        return fromDict(cls, data)

    def __post_init__(self):
        if not self.path.is_file():
            raise FileNotFoundError()

    def dumps(self) -> str:
        return (
            r"\includegraphics[width= 0.18\textwidth]{"
            + str(self.path)
            + r"}\\\usekomavar{fromname}"
        )
