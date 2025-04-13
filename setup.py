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


version = os.environ.get("PYPI_TAG")

semver_regex = r"^v?\d+\.\d+\.\d+$"
if not version:
    raise ValueError("PYPI_TAG environment variable is not set.")

if not re.match(semver_regex, version):
    raise ValueError(f"Git tag '{version}' is not a valid, e.g. 1.2.3 ")

setup(
    name="test_app_hommat",
    version=version,
    description="A test library.",
    packages=find_packages(),
    # install_requires=read_file("requirements.txt").splitlines(),
    # long_description=read_file("README.md"),
    # long_description_content_type="text/markdown",
)
