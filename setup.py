#! /usr/bin/env python

from setuptools import setup
import sys

PACKAGE = "seqcolapi"

# Additional keyword arguments for setup().
extra = {}

# Ordinary dependencies
DEPENDENCIES = []
with open("requirements/requirements-all.txt", 'r') as reqs_file:
    for line in reqs_file:
        print(line)
        if not line.strip():
            continue
        DEPENDENCIES.append(line)

# 2to3
if sys.version_info >= (3, ):
    extra["use_2to3"] = True
extra["install_requires"] = DEPENDENCIES


with open("{}/_version.py".format(PACKAGE), 'r') as versionfile:
    version = versionfile.readline().split()[-1].strip("\"'\n")


# Handle the pypi README formatting.
try:
    import pypandoc
    long_description = pypandoc.convert_file('README.md', 'rst')
    msg = "\033[032mPandoc conversion succeeded.\033[0m"
except(IOError, ImportError, OSError):
    msg = "\033[0;31mWarning: pandoc conversion failed!\033[0m"
    long_description = open('README.md').read()


setup(
    name=PACKAGE,
    packages=[PACKAGE],
    version=version,
    description="API for Sequence Collections",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Scientific/Engineering :: Bio-Informatics"
    ],
    keywords=" bioinformatics, sequencing, ngs, genomes, server",
    url="https://seqcol.databio.org/",
    author=u"Nathan Sheffield",
    license="BSD2",
    entry_points={
        "console_scripts": [
            "{p} = {p}.__main__:main".format(p=PACKAGE),
        ],
    },
    include_package_data=True,
    **extra
)

print(msg)