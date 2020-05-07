from setuptools import setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="ydatecount",
    version="1.0",
    description="A programme for days calculation.",
    license="GPLv3",
    long_description=long_description,
    author="Yang Yunyi",
    author_email="badboy1616@protonmail.com",
    url="https://github.com/Badboy-16/y-datecount",
    packages="ydatecount",
    python_requires=">=3.6",
)
