"""Setup script for opcreader project"""

import os.path
from setuptools import setup

THIS_FOLDER = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(THIS_FOLDER, "README.md")) as fhandle:
    README_TEXT = fhandle.read()

setup(
    name="opcreader",
    version="1.0.0",
    description="Read OPC metadata from an OPC package (file)",
    long_description=README_TEXT,
    long_description_content_type="text/markdown",
    url="https://github.com/dmahugh/python-exe-sample",
    author="Doug Mahugh",
    author_email="dmahugh@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
    packages=["opcreader"],
    include_package_data=True,
    install_requires=["importlib_resources"],
    entry_points={"console_scripts": ["opcinfo=opcreader.__main__:main"]},
)
