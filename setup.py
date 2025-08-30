from setuptools import setup, find_packages

setup(
    name="myapp",  # <-- CHANGE THIS
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests",  # example dependency, adjust as needed
    ],
)
