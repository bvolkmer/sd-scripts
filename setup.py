from pathlib import Path

from setuptools import find_packages, setup

setup(
    name="library",
    packages=find_packages(),
    install_requires=list(
        filter(
            lambda x: not x.startswith("#"),
            Path("./requirements.txt").read_text().splitlines(),
        )
    ),
)

