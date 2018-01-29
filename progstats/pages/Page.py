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
from progstats import template_path


class Page(object):
    """
    Class that models a page
    """

    def __init__(self, name: str):
        """
        Initializes the page, loads the HTML template
        :param name: The name of the page, used to find the HTML template
        """
        self.name = name
        self.html_file = os.path.join(template_path, name + ".html")

        with open(self.html_file, "r") as f:
            self.html = f.read()

    def insert(self, content: str, tag: str):
        """
        Inserts content into the HTML template
        Replaces @{TAG}s in the HTML with the specified content
        :param content: The content to insert
        :param tag: The tag to replace
        :return: None
        """
        self.html = self.html.replace("@{" + tag + "}", content)

    def render(self):
        """
        Renders the page
        :return: None
        """
        print("Content-Type: text/html")
        print()
        print(self.html)