"""LICENSE
Copyright 2018 Hermann Krumrey <hermann@krumreyh.com>

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
LICENSE"""

import os
from enum import Enum
from flask import abort


class TopicType(Enum):
    """
    An enumeration modelling all possible topic types
    """
    GITSTATS = ("gitstats", "@{project}/index.html")
    GIT_STATS = ("git_stats", "@{project}/index.html")
    COVERAGE = ("coverage", "@{project}/index.html")
    DOC_HTML = ("doc_html", "@{project}/index.html")
    DOC_PDF = ("doc_pdf", "@{project}.pdf")


class Topic:
    """
    Models a topic
    """

    def __init__(self, root_dir: str, topic_type: TopicType):
        """
        Initializes the topic
        :param root_dir: The root data directory path
        :param topic_type:
        """
        self.name, self.target = topic_type.value
        self.path = os.path.join(root_dir, self.name)

    def generate_path(self, project_name: str) -> str:
        """
        Generates the path to a project's data resource
        :param project_name: The name of the project
        :return: The path to the resource
        """
        if project_name == "":
            abort(404)

        return os.path.join(
            self.name,
            self.target.replace("@{project}", project_name)
        )

    def __eq__(self, other):
        """
        Checks for equality with another object
        :param other: The other object to check
        :return: True if the objects are equal, False otherwise
        """
        try:
            return self.path == other.path \
                and self.name == other.name \
                and self.target == other.target
        except AttributeError:
            return False
