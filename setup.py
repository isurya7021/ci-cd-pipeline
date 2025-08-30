import os
from setuptools import setup, find_packages

# Get version from Jenkins environment variable (BUILD_VERSION)
VERSION = os.getenv("BUILD_VERSION", "0.1.0")

setup(
    name="myapp",  # <-- change if your app has a different name
    version=VERSION,
    packages=find_packages(),
    install_requires=[
        "requests",  # example dependency
    ],
    entry_points={
        "console_scripts": [
            "myapp = myapp.__main__:main"  # so ExecStart can run `myapp`
        ]
    },
)
