#!/usr/bin/env python

from setuptools import setup

setup(
    name="multlanguages",
    version="0.8.0",
    packages=["multlanguages"],
    setup_requires=['setuptools_scm'],
    author="SHENOISZ",
    author_email="marcelo.net.system@gmail.com",
    description="django-multlanguages for Python Django",
    platforms="Any",
    license="django-multlanguages",
    keywords="translations, hosts, language",
    url="https://github.com/SHENOISZ/django-multlanguages",
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.9',
        str("Programming Language :: Python :: 2"),
        str("Programming Language :: Python :: 2.7"),
        str("Programming Language :: Python :: 3"),
        str("Programming Language :: Python :: 3.2"),
        str("Programming Language :: Python :: 3.3"),
        str("Programming Language :: Python :: 3.4"),
    ]
)
