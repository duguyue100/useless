import platform
import sys

from setuptools import find_packages
from setuptools import setup


python_min_version = (3, 10, 0)
python_min_version_str = ".".join(map(str, python_min_version))
if sys.version_info < python_min_version:
    print(
        "You are using Python {}. Python >={} is required.".format(
            platform.python_version(), python_min_version_str
        )
    )
    sys.exit(-1)

setup(
    name="uselesss",
    version="0.0.1",
    description="There are too many useful things out there. This is a useless package.",
    author="Yuhuang Hu",
    license="MIT",
    packages=find_packages(exclude=["tests"]),
)
