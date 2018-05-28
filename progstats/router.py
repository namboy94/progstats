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

from flask import Flask, render_template, abort, request
from progstats.entities import get_topics, get_projects

app = Flask(__name__)


@app.route("/")
def index():
    """
    The Home page of the website. Will display the /project/ page.
    :return: The /projects/ page
    """
    return render_template("home.html")


@app.route("/projects/")
@app.route("/projects/<project_name>")
def projects(project_name: str = None):
    """
    Lists all projects or displays details about a single project
    :param project_name: The name of the project to display.
    :return: An HTML document containing a list of projects
             or the details of the selected project
    """
    all_projects = get_projects()
    if project_name is None:
        return render_template(
            "lister.html", lister_type="Projects", items=all_projects
        )

    else:
        filtered = list(filter(lambda x: x.name == project_name, all_projects))
        if len(filtered) != 1:
            abort(404)
        else:
            return render_template(
                "project.html", host=request.host_url, project=filtered[0]
            )


@app.route("/topics/")
@app.route("/topics/<topic_name>")
def topics(topic_name: str = None):
    """
    Displays a list of all available topics or a list of projects that
    offer info on a specified topic
    :param topic_name: The name of the topic to display
    :return: The page containing all available topics or the projects
             applicable to a topic
    """
    all_topics = get_topics()
    if topic_name is None:
        return render_template(
            "lister.html", lister_type="Topics", items=all_topics
        )

    else:
        filtered = list(filter(lambda x: x.name == topic_name, all_topics))

        if len(filtered) != 1:
            abort(404)
        else:
            topic = filtered[0]
            topic_projects = list(filter(
                lambda x: topic in x.topics,
                get_projects()
            ))
            print(topic_projects)
            return render_template(
                "topic.html",
                topic=topic,
                projects=topic_projects,
                host=request.host_url
            )


@app.route("/test")
def test():
    return request.host_url.rsplit(":", 1)[0]
