from dataclasses import dataclass
from datetime import datetime

import babel.dates

from .utils import fromDict


@dataclass
class DateAndLocation:
    date: datetime
    city: str

    date_format: str = "dd. MMMM yyyy"
    date_location: str = "de_DE"

    @classmethod
    def fromDict(cls, data):

        def date_parsing(date: str):
            if date.lower() == "today":
                return datetime.now()
            raise NotImplementedError()

        return fromDict(cls, data, special_parsing={"date": date_parsing})

    def dumps_date(self) -> str:
        tmp = babel.dates.format_datetime(self.date,
                                          self.date_format,
                                          locale=self.date_location)
        return tmp

    def dumps_location(self) -> str:
        return self.city
