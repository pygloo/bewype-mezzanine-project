#!/usr/bin/env python
# -*- coding: utf-8 -*-

# setuptools import
from setuptools import setup, find_packages

version = "0.1"

setup(
    name="mezzype",
    version=version,
    author="Florent Pigout",
    author_email="florent.pigout@bewype.org",
    description="Bewype Mezzanine Project",
    long_description="",
    license = "MIT",
    url="http://www.bewype.org",
    packages=find_packages(exclude=[]),
    package_data = {},
    data_files=["COPYING"],
    zip_safe=False,
    include_package_data=True,
    install_requires=[
        "cartridge",
        "south",
        "pil",
        "django-userena",
        "emencia.django.countries",
        ],
    namespace_packages=[
        ],
    entry_points="""
    """,
    )

