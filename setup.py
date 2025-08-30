import os
from setuptools import setup, find_packages

# Get version from Jenkins (BUILD_VERSION), fallback to default
VERSION = os.getenv("BUILD_VERSION", "0.1.0")

setup(
    name="myapp",
    version=VERSION,
    packages=find_packages(),
    install_requires=[
        "requests",  # example dependency
    ],
    entry_points={
        "console_scripts": [
            "myapp = myapp.__main__:main",  # lets you run "myapp"
        ]
    },
    python_requires=">=3.6",
)
