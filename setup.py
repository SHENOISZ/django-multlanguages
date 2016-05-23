#!/usr/bin/python
import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

PACKAGE = "django-mult-languages"
NAME = "django-mult-languages"
DESCRIPTION = "Django package util translation"
AUTHOR = "SHENOISZ"
AUTHOR_EMAIL = "marcelo.net.system@gmail.com"
URL = "https://github.com/SHENOISZ/django-multlanguages"
VERSION = __import__("mult_languages").__version__

setup(
    name=NAME,
    packages = find_packages(),
    version=VERSION,
    description=DESCRIPTION,
    long_description=read("README.rst"),
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    license="BSD",
    url=URL,
    # packages=["tests.*", "tests"],
    classifiers=[
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Framework :: Django",
    ],
    keywords = ["translation", "translations", "hosts"],
)
