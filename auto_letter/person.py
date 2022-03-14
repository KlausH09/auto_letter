from dataclasses import dataclass

from .utils import fromDict


@dataclass
class Person:
    salutation: str
    surename: str
    lastname: str
    title: str = None

    @classmethod
    def fromDict(cls, data):
        return fromDict(cls, data)

    @property
    def full_name(self) -> str:
        if self.title is None:
            return f"{self.surename} {self.lastname}"
        return f"{self.title} {self.surename} {self.lastname}"

    @property
    def full_salutation(self) -> str:
        if self.title is None:
            return f"{self.salutation} {self.surename} {self.lastname}"
        return f"{self.salutation} {self.title} {self.surename} {self.lastname}"
