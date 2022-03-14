from typing import List
from dataclasses import dataclass

from .utils import fromDict


@dataclass
class Address:
    street: str
    city: str
    postcode: str

    @classmethod
    def fromDict(cls, data):
        return fromDict(cls, data)

    @property
    def full_address(self) -> List[str]:
        return [self.street, f"{self.postcode} {self.city}"]
