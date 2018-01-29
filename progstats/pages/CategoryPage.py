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
from progstats.pages.Page import Page
from progstats import content_path


class CategoryPage(Page):
    """
    Page that lists all content in a content directory
    """

    def __init__(self, name: str, path: str):
        """
        Initializes the page
        :param name: The name of the page
        :param path: The path to the category's content
        """
        super().__init__("category")

        identifier = "index.html"
        if path in ["documentation-pdf"]:
            identifier = "documentation.pdf"

        content_list = ""
        category_dir = os.path.join(content_path, path)
        for project in sorted(os.listdir(category_dir)):

            search_file = os.path.join(category_dir, project, identifier)
            relative = os.path.join("content", project, identifier)

            if os.path.isfile(search_file):
                content_list += "<a href=\"" + relative + "\">"
                content_list += project
                content_list += "</a>"

        self.insert(name, "NAME")
        self.insert(content_list, "CONTENT_LIST")
