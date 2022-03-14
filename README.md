# auto_letter

[![codecov](https://codecov.io/gh/KlausH09/auto_letter/branch/main/graph/badge.svg?token=auto_letter_token_here)](https://codecov.io/gh/KlausH09/auto_letter)
[![CI](https://github.com/KlausH09/auto_letter/actions/workflows/main.yml/badge.svg)](https://github.com/KlausH09/auto_letter/actions/workflows/main.yml)

Create letters from JSON

## Install

```bash
pip install git+https://github.com/KlausH09/auto_letter.git@main
```

## Usage

```py
import json
from auto_letter import LetterGen

with open("example.json", "r", encoding="utf8") as fd:
    letter_data = json.load(fd)

letterGen = LetterGen.fromDict(letter_data)
doc = letterGen.dump()

# tex = doc.dumps()
# doc.generate_tex("out")
doc.generate_pdf("out", clean_tex=False, compiler="pdflatex")
```

```bash
python -m auto_letter ./example.json ./out
```
