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
from progstats import resource_path, content_path, template_path


class CategoryPage(object):

    def __init__(self, identifier: str):
        with open(os.path.join(template_path, identifier + ".html"), "r") as f:
            self.html = f.read()

    def render(self):
        print("Content-Type: text/html")
        print()
        print(self.html)
