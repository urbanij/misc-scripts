#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Sun Nov  3 19:03:45 CET 2019

from distutils.core import setup
from Cython.Build import cythonize

setup(ext_modules=cythonize('functions.pyx'))


