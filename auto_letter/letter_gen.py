from dataclasses import dataclass

from pylatex import Document, Command, Package
from pylatex.base_classes import Environment
from pylatex.utils import NoEscape

from .sender import Sender
from .recipient import Recipient
from .date_and_location import DateAndLocation
from .utils import setkomavar, fromDict


@dataclass
class LetterGen:
    sender: Sender
    recipient: Recipient

    date_and_location: DateAndLocation
    subject: str

    opening: dict  # Dict[str, str]
    content: str
    closing: str

    @classmethod
    def fromDict(cls, data):
        def content_parsing(data):
            if isinstance(data, list):
                data = "\n".join(data)
            return str(data)
        return fromDict(cls, data, special_parsing={"content": content_parsing})

    def _get_opening(self) -> Command:
        person = self.recipient.person
        if person is None:
            tmp = f"{self.opening[str(None)]},"
        else:
            tmp = f"{self.opening[str(person.salutation)]} {person.full_salutation},"
        return Command("opening", tmp)

    def _get_content(self) -> NoEscape:
        return NoEscape(self.content)

    def _get_closing(self) -> Command:
        return Command("closing", self.closing)

    def dump(self) -> Document:
        doc = self._create_base_doc()

        self.sender.dump(doc)
        doc.append(setkomavar("date", self.date_and_location.dumps_date()))
        doc.append(setkomavar("place", self.date_and_location.dumps_location()))
        doc.append(setkomavar("subject", self.subject))

        class letter(Environment):
            packages = []
            escape = False
            content_separator = "\n"

        with doc.create(letter(arguments=self.recipient.dumps())):
            doc.append(self._get_opening())
            doc.append(self._get_content())
            doc.append(self._get_closing())

        return doc

    def _create_base_doc(self) -> Document:
        doc = Document(
            documentclass="scrlttr2",
            document_options=[
                "fontsize=12pt",  # Schriftgröße
                "parskip=full",  # zwischen Absätzen eine leere Zeile einfügen, statt lediglich Einrückung
                "paper=A4",  # Papierformat auf DIN-A4
                "fromalign=right",  # Briefkopf(ganz oben) rechts ausrichten, standardmäßig links
                "fromphone=true",  # Telefonnummer im Briefkopf anzeigen
                "fromemail=true",  # E-Mail-Adresse im Briefkopf anzeigen
                "version=last",  # Die neuste Version von scrlettr2 verwenden
            ],
        )

        doc.preamble.append(Package("babel", "ngerman"))
        doc.preamble.append(Package("hyperref", "hidelinks"))
        doc.preamble.append(Package("graphicx"))

        doc.preamble.append(NoEscape(r""))
        doc.preamble.append(NoEscape(r"% Euro Symbol-Support"))
        doc.preamble.append(Package("eurosym"))
        doc.preamble.append(Command("DeclareUnicodeCharacter", ["20AC", NoEscape(r"\euro")]))

        if self.sender.signature is not None:
            doc.preamble.append(NoEscape(r""))
            doc.preamble.append(NoEscape(r"% Distance between closing and name"))
            doc.preamble.append(Command("makeatletter"))
            doc.preamble.append(Command("@setplength", ["sigbeforevskip", "0.5em"]))
            doc.preamble.append(Command("makeatother"))

        doc.preamble.append(NoEscape(r""))
        doc.preamble.append(NoEscape(r"% no indent after closing"))
        doc.preamble.append(Command("renewcommand*", [NoEscape(r"\raggedsignature"),
                                                      NoEscape(r"\raggedright")]))

        return doc
