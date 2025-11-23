from pathlib import Path
from setuptools import setup, find_packages

README = Path(__file__).parent / "README.md"

setup(
    name="sithaxa",
    version="0.0.0.2",
    author="adubiblessed",
    author_email="adubiblessed@gmail.com",
    description="Sithaxa - AI-powered local CLI coding assistant",
    long_description=README.read_text(encoding="utf-8"),
    long_description_content_type="text/markdown",
    packages=find_packages(exclude=("tests",)),
    python_requires=">=3.8",
    install_requires=[
        "typer>=0.20.0",
        "rich>=14.2.0",
    ],
    entry_points={
        "console_scripts": [
            "sithaxa=sithaxa.cli.main:app",
        ],
    },
)
