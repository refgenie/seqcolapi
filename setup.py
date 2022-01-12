#! /usr/bin/env python

import os
import sys
from setuptools import setup

# Configuration options edit
cfg = {
    "package_name": "seqcolapi",
    "author": u"Nathan Sheffield",
    "author_email": "nathan@code.databio.org",
    "description": "API for Sequence Collections",
    "license": "BSD2",
    "keywords": "bioinformatics, sequencing, ngs, genomes, server",
    "requirements_file": "requirements/requirements-all.txt",
    "url": "https://seqcol.databio.org/",
    "classifiers": [
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
    ],
}

# -----------------------------------------------------------------------------
# Boilerplate below here should not require editing

extra = {}
reqs = []  # requirements array
with open(cfg["requirements_file"], "r") as reqs_file:
    for line in reqs_file:
        if not line.strip():
            continue
        reqs.append(line)
extra["install_requires"] = reqs

with open(os.path.join(cfg["package_name"], "_version.py"), "r") as versionfile:
    version = versionfile.readline().split()[-1].strip("\"'\n")

with open("README.md") as f:
    long_description = f.read()
    
setup(
    name=cfg["package_name"],
    packages=[cfg["package_name"]],
    version=version,
    description=cfg["description"],
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=cfg["classifiers"],
    license=cfg["license"],
    keywords=cfg["keywords"],
    url=cfg["url"],
    author=cfg["author"],
    author_email=cfg["author_email"],
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "{p} = {p}.__main__:main".format(p=cfg["package_name"]),
        ],
    },
    **extra
)
