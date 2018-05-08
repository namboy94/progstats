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
from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    """
    The Home page of the website. Will display the /project/ page.
    :return: The /projects/ page
    """
    return os.environ["PROGSTATS_DATA"]


@app.route("/projects/")
def projects():
    """
    Lists all projects.
    :return: An HTML document containing a list of projects
    """
    return "projects"


@app.route("/projects/<project_name>")
def project(project_name: str):
    """
    Displays details about a single project
    :param project_name: The name of the project
    :return: The project's page
    """
    return project_name


@app.route("/topics/")
def topics():
    """
    Displays a list of all available topics
    :return: The page containing all available topics
    """
    return "topics"


@app.route("/topics/<topic_name>")
def topic(topic_name: str):
    """
    Displays a list of projects that offer info on a topic
    :param topic_name: The name of the topic
    :return: The topic's list of projects
    """
    return topic_name
