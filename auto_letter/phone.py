from dataclasses import dataclass

from .utils import fromDict


@dataclass
class Phone:
    data: str

    @classmethod
    def fromDict(cls, data):
        return fromDict(cls, data)

    def dumps(self) -> str:
        return r"\href{tel:" + str(self.data) + r"}{" + str(self.data) + r"}"
