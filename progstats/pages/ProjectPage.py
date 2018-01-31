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
from progstats.pages.ProjectsPage import ProjectsPage


class ProjectPage(Page):
    """
    Page that either lists all projects or shows all stats for a project
    """

    def __init__(self, project_name: str = None):
        super().__init__("project")

        project_data = ProjectsPage.traverse_content()
        html_data = "<ul>"

        if project_name is None or project_name not in project_data:
            self.insert("All Projects", "PROJECT_NAME")
            for project in sorted(project_data.keys()):
                html_data += "<li><a href=\"project.py?name=" + project + "\">"
                html_data += project + "</a></li>"

        else:
            self.insert(project_name, "PROJECT_NAME")
            project = project_data[project_name]
            for category in sorted(project.keys()):
                html_data += "<li><a href=\"" + project[category] + "\">"
                html_data += category + "</a></li>"

        html_data += "</ul>"
        self.insert(html_data, "CONTENT")
