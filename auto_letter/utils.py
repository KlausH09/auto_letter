from pylatex import Command
from pylatex.utils import NoEscape


def setkomavar(name, value) -> Command:
    return Command("setkomavar", [name, NoEscape(value)])


def fromDict(cls, data, special_parsing=None):
    if special_parsing is None:
        special_parsing = {}
    tmp = {}
    for name, info in cls.__dataclass_fields__.items():
        if name not in data:
            continue

        raw_field_data = data[name]

        if raw_field_data is None:
            tmp[name] = raw_field_data
        elif name in special_parsing:
            tmp[name] = special_parsing[name](raw_field_data)
        elif hasattr(info.type, "fromDict"):
            tmp[name] = info.type.fromDict(raw_field_data)
        else:
            tmp[name] = info.type(raw_field_data)

    return cls(**tmp)
