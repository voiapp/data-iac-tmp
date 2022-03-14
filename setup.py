"""Setup file for data-iac"""
from setuptools import find_packages, setup

setup(
    name="data-iac",
    version="0.1.1",
    description="data-iac",
    author="Data-platform team",
    author_email="data-platform@voiapp.io",
    url="https://www.python.org/sigs/distutils-sig/",
    packages=[*find_packages(exclude=["test", "test.*"])],
    entry_points={"console_scripts": ["iac_cli= iac_cli.__main__:main"]},
)
