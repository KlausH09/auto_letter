import json
import argparse  # pragma: no cover

from . import LetterGen  # pragma: no cover

if __name__ == "__main__":  # pragma: no cover

    parser = argparse.ArgumentParser(description="Create letters from JSON")
    parser.add_argument("json_file", type=str, help="path to the JSON file")
    parser.add_argument("output_path", type=str, help="path to save the PDF", default="./out")
    args = parser.parse_args()

    with open(args.json_file, "r", encoding="utf8") as fd:
        letter_data = json.load(fd)

    letterGen = LetterGen.fromDict(letter_data)
    doc = letterGen.dump()

    # tex = doc.dumps()
    # doc.generate_tex(args.output_path)
    doc.generate_pdf(args.output_path, clean_tex=False, compiler="pdflatex")
