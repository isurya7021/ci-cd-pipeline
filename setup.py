import os
from setuptools import setup, find_packages

VERSION = os.getenv("BUILD_VERSION", "0.1.0")

setup(
    name="myapp",
    version=VERSION,
    packages=find_packages(),
    install_requires=[
        "requests",
    ],
)
