#!/usr/bin/python
import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

PACKAGE = "multlanguages"
NAME = "multlanguages"
DESCRIPTION = "Django package util translation"
AUTHOR = "SHENOISZ"
AUTHOR_EMAIL = "marcelo.net.system@gmail.com"
URL = "https://github.com/SHENOISZ/django-multlanguages"
VERSION = __import__(PACKAGE).__version__

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=read("README.rst"),
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    license="BSD",
    url=URL,
    # packages=["tests.*", "tests"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Framework :: Django",
    ],
    zip_safe=False,
)
