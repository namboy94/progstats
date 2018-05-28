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
from typing import List
from progstats.entities.Project import Project
from progstats.entities.Topic import Topic, TopicType


def get_topics() -> List[Topic]:
    """
    Retrieves a list of all available topics
    :return: The list of topics
    """
    data_dir = os.environ["PROGSTATS_DATA"]

    topics = []
    for topic in os.listdir(data_dir):

        if topic.startswith("."):
            continue

        for topic_type in TopicType:
            if topic_type.value[0] == topic:
                topics.append(Topic(data_dir, topic_type))
    topics.sort(key=lambda x: x.name)
    return topics


def get_projects() -> List[Project]:
    """
    Retrieves a list of all projects
    :return: The list of projects
    """

    topics = get_topics()
    projects = {}

    for topic in topics:
        for project_name in os.listdir(topic.path):

            if project_name.startswith("."):
                continue
            if project_name.endswith(".pdf"):
                project_name = project_name.rsplit(".pdf", 1)[0]

            if project_name in projects:
                projects[project_name].add_topic(topic)
            else:
                projects[project_name] = Project(project_name, [topic])

    project_list = []
    for project in projects:
        project_list.append(projects[project])

    project_list.sort(key=lambda x: x.name)
    return project_list
