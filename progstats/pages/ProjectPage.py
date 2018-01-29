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


class ProjectPage(Page):
    """
    Page that lists the projects in a table
    """

    def __init__(self):
        super().__init__("projects")
        content = self.traverse_content()

        table_header = "<tr><th>Project</th>"
        categories = list(sorted(os.listdir(content_path)))
        for category in categories:
            table_header += "<th>" + category + "</th>"

        self.insert(table_header, "TABLE_HEADER")

        table_rows = ""

        for project_name in sorted(content.keys()):
            project_data = content[project_name]

            table_rows += "<tr><th>" + project_name + "</th>"

            for category in categories:
                table_rows += "<th>"

                if category in project_data:
                    table_rows += "<a href=\"" + project_data[category]
                    table_rows += "\">Link</a>"
                else:
                    table_rows += "N/A"

                table_rows += "</th>"

        self.insert(table_rows, "TABLE_ROWS")

    # noinspection PyMethodMayBeStatic
    def traverse_content(self) -> dict:
        project_data = {}

        for category in os.listdir(content_path):
            for project in os.listdir(os.path.join(content_path, category)):

                if project.startswith("."):
                    continue

                project_path = os.path.join(content_path, category, project)
                project_rel_path = os.path.join("content", category, project)

                if os.path.isfile(project_path):
                    project_name = project.rsplit(".", 1)[0]
                else:
                    project_name = project

                if project_name not in project_data:
                    project_data[project_name] = {}

                if os.path.isfile(os.path.join(project_path, "index.html")):
                    project_data[project][category] =\
                        os.path.join(project_rel_path, "index.html")

                elif os.path.isfile(project_path):
                    project_data[project][category] = project_rel_path

        return project_data
