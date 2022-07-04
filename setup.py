#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Setup script.
"""

from setuptools import find_packages, setup
from pathlib import Path


def read_requirements(path):
    """read requirements"""
    return list(Path(path).read_text().splitlines())


base_reqs = read_requirements("requirements/core.txt")
docs_reqs = read_requirements("requirements/paddle.txt")

all_reqs = base_reqs + docs_reqs

setup(
   name='hktest_readthedocs',
   version='0.1.0',
   maintainer='hktest_readthedocs',
   maintainer_email='hkhuoke@hotmail.com',
   packages=find_packages(),
   url='',
   license='LICENSE.txt',
   description="hktest_readthedocs project description.",
   long_description=open('README.md').read(),
   install_requires=base_reqs,
   extras_require={
       "docs": docs_reqs,
       "all": all_reqs
    }
)

