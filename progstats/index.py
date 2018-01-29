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

print("Content-Type: text/html")
print()

file_path = os.path.dirname(__file__)
template = os.path.join(file_path, '..', "resources", "html", "index.html")

with open(template, "r") as template_file:
    html = template_file.read()

category_html = ""
for category in ["gitstats", "git_stats", "coverage",
                 "documentation", "documentation-pdf"]:
    category_html += "<h3><a href=\"" + category + ".py\">" + category + \
                     "</a></h3>"

html = html.replace("@{CATEGORIES}", category_html)
print(html)
