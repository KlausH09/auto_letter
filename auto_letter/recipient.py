from dataclasses import dataclass

from pylatex.utils import NoEscape

from .person import Person
from .address import Address

from .utils import fromDict


@dataclass
class Recipient:
    company: str
    address: Address
    person: Person = None

    @classmethod
    def fromDict(cls, data):
        return fromDict(cls, data)

    def dumps(self) -> NoEscape:
        tmp = [self.company]
        if self.person is not None:
            tmp.append(self.person.full_salutation)
        tmp += self.address.full_address
        return NoEscape(r"\\".join(tmp))
