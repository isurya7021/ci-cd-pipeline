from setuptools import setup, find_packages

setup(
    name="my-python-app",
    version="1.0.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        # Add runtime dependencies here
    ],
    entry_points={
        "console_scripts": [
            "my-python-app=my_python_app.main:main",
        ],
    },
)
