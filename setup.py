from setuptools import setup, find_packages

setup(
    name="myapp",
    version="1.0.1",
    packages=find_packages(),  # <- this includes your myapp/ directory
    install_requires=[
        "requests",
    ],
    entry_points={
        "console_scripts": [
            "myapp=myapp.main:main",  # if you have a main.py
        ]
    },
)
