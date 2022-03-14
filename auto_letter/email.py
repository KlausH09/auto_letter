from dataclasses import dataclass

from .utils import fromDict


@dataclass
class EMail:
    data: str

    @classmethod
    def fromDict(cls, data):
        return fromDict(cls, data)

    def dumps(self) -> str:
        return r"\href{mailto:" + str(self.data) + r"}{" + str(self.data) + r"}"
