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
from progstats.entities.Topic import Topic


class Project:
    """
    Models a project
    """

    def __init__(self, name: str, topics: List[Topic]):
        """
        Initializes the project
        :param name: The name of the project
        :param topics: The topics available for this project
        """
        self.name = name
        self.topics = topics
        self.topics.sort(key=lambda x: x.name)

    def get_target(self, host: str, topic: Topic) -> str or None:
        """
        Generates the target URL to the data resource for a specified topic
        :param host: The host's root URL
        :param topic: The topic to generate the target path for
        :return: The generated path, or None if the specified topic does not
                 apply to this project
        """
        if topic not in self.topics:
            return

        else:
            return os.path.join(
                host,
                "data",
                topic.generate_path(self.name)
            )

    def add_topic(self, topic: Topic):
        """
        Adds a topic to the project
        :param topic: The topic to add
        :return: None
        """
        if topic not in self.topics:
            self.topics.append(topic)
        self.topics.sort(key=lambda x: x.name)

    def __eq__(self, other):
        """
        Checks the Project anime for equality with another object
        :param other: The object to check for equality against
        :return: True if equal, else False
        """
        try:
            return self.name == other.name
        except AttributeError:
            return False
