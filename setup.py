"""
Copyright 2018 Hermann Krumrey

This file is part of progstats.

progstats is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

progstats is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with progstats.  If not, see <http://www.gnu.org/licenses/>.
"""

# imports
from progstats import version
from setuptools import setup, find_packages


setup(
    name="progstats",
    version=version,
    description="An website that display programming stats",
    long_description=open("README.md").read(),
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)"
    ],
    url="https://gitlab.namibsun.net/namboy94/progstats",
    download_url="https://gitlab.namibsun.net/namboy94/progstats/"
                 "repository/archive.zip?ref=master",
    author="Hermann Krumrey",
    author_email="hermann@krumreyh.com",
    license="GNU GPL3",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["flask"],
    test_suite='nose.collector',
    tests_require=['nose'],
    zip_safe=False
)