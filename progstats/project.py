#!/usr/bin/env python3
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

import os
import sys
import cgi
sys.path.insert(0, os.path.abspath(".."))


def main():
    """
    Displays the project page
    :return: None
    """
    from progstats.pages.ProjectPage import ProjectPage
    try:
        args = cgi.FieldStorage()
        ProjectPage(args["name"].value).render()
    except KeyError:
        ProjectPage().render()


if __name__ == "__main__":
    main()
