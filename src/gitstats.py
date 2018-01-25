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
print("<h1>gitstats</h1>")

content_path = os.path.join(os.path.dirname(__file__), "..", "content")
gitstats = os.path.join(content_path, "gitstats")

for project in os.listdir(gitstats):
    project_index = os.path.join(gitstats, project, "index.html")

    if os.path.isfile(project_index):
        print("<a href=\"" + project_index + "\">" + project + "</a>")
