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

from progstats.pages.Page import Page


class IndexPage(Page):
    """
    Models the Index page
    """

    def __init__(self):
        """
        Initializes the content of the index page
        """
        super().__init__("index")

        categories = {
            "Git Statistics": {
                "gitstats": "gitstats",
                "git_stats": "git_stats"
            },
            "Documentation": {
                "HTML Documentation": "documentation-html",
                "PDF Documentation": "documentation-pdf"
            },
            "Test Coverage": {
                "Coverage": "coverage"
            }
        }

        categories_html = ""
        for category in sorted(categories.keys()):
            categories_html += "<h2>" + category + "</h2>"
            for subcategory in sorted(categories[category].keys()):
                path = categories[category][subcategory]
                url = "category.py?name=" + subcategory + "&path=" + path
                categories_html += "<h4><a href=\"" + url + "\">" + subcategory
                categories_html += "</a></h4>"

        self.insert(categories_html, "CATEGORIES_LIST")
