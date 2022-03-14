"""Python setup.py for auto_letter package"""
from typing import List

from setuptools import find_packages, setup


def read(path: str) -> str:
    """Read a file

    Args:
        path (str): path to the file

    Returns:
        str: content of the file
    """
    with open(path, "r", encoding="utf8") as fd:
        return fd.read().strip()


def read_requirements(path: str) -> List[str]:
    """Read a requirements file

    Args:
        path (str): path to the file

    Returns:
        List[str]: requirements
    """
    def is_valid(x: str):
        return len(x) > 0 and not x.startswith(("#",))
    return [x.strip() for x in read(path).split("\n") if is_valid(x)]


setup(
    name="auto_letter",
    version=read("auto_letter/VERSION"),
    description="Awesome auto_letter created by KlausH09",
    url="https://github.com/KlausH09/auto_letter/",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="KlausH09",
    packages=find_packages(exclude=["tests", ".github"]),
    install_requires=read_requirements("requirements.txt"),
    entry_points={
        "console_scripts": ["auto_letter = auto_letter.__main__:main"]
    },
    extras_require={"test": read_requirements("requirements-dev.txt")},
)
