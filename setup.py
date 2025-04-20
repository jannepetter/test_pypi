"""
Setup file for Pypi.
"""

import os
import re
from setuptools import setup, find_packages


def read_file(filename: str):
    """
    Helper to read files.
    """
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()


version = os.environ.get("PYPI_TAG", "v0.0.0")
semver_regex = r"^v\d+\.\d+\.\d+$"

if not re.match(semver_regex, version):
    raise ValueError(f"Git tag '{version}' is not a valid, e.g. v1.2.3 ")

version = version[1:]

setup(
    name="test_app_hommat",
    version=version,
    description="A test library.",
    packages=find_packages(),
    # install_requires=read_file("requirements.txt").splitlines(),
    # long_description=read_file("README.md"),
    # long_description_content_type="text/markdown",
)
