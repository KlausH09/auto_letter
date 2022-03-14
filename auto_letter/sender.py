from dataclasses import dataclass
from typing import List

from pylatex import Document, Command

from .person import Person
from .address import Address
from .phone import Phone
from .email import EMail
from .signature import Signature
from .utils import setkomavar, fromDict


@dataclass
class Sender:
    person: Person
    address: Address
    phone: Phone
    email: EMail
    signature: Signature = None

    @classmethod
    def fromDict(cls, data):
        return fromDict(cls, data)

    def dumps(self) -> List[Command]:
        tmp = [
            setkomavar("fromname", self.person.full_name),
            setkomavar("fromaddress", r"\\".join(self.address.full_address)),
            setkomavar("fromphone", self.phone.dumps()),
            setkomavar("fromemail", self.email.dumps()),
        ]
        if self.signature is not None:
            tmp.append(setkomavar("signature", self.signature.dumps()))
        return tmp

    def dump(self, doc: Document):
        for c in self.dumps():
            doc.append(c)
