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
import shutil
import argparse
from subprocess import Popen


def main():
    """
    The main method of this script. Parses the arguments from the command
    line and processes them.

    The Method starts by cloning the gitlab-cloner script. Using that, all
    repositories of the user's gitlab account are cloned (or pulled if they
    already exist). Afterwards, git_stats and gitstats will be run on the
    repositories. After that, unittest.sh and documentation-pdf.sh scripts will
    be executed if present.

    The resulting outputs will be stored in the "output" directory in the
    current working directory
    :return: None
    """

    parser = argparse.ArgumentParser()
    parser.add_argument("url", help="The Gitlab URL to use")
    parser.add_argument("username", help="The Gitlab username")
    parser.add_argument("token", help="The Gitlab API token")
    parser.add_argument("-c", "--cleanup",
                        help="Deletes all temporary files after the generation"
                             " completes.")
    args = parser.parse_args()

    if os.path.exists("gitlab-cloner"):
        shutil.rmtree("gitlab-cloner")
    Popen([
        "git", "clone",
        "https://gitlab.namibsun.net/namboy94/gitlab-cloner.git"
    ]).wait()

    for category in [
        "gitstats",
        "git_stats",
        "coverage",
        "documentation-pdf",
        "documentation-pdf-pdf"
    ]:
        directory = os.path.join("output", category)
        if os.path.exists(directory):
            shutil.rmtree(directory)
        os.makedirs(directory)

    Popen([
        "python",
        "gitlab-cloner/gitlab-cloner.py",
        "-d", "repos",
        args.url, args.username, args.token
    ]).wait()
    shutil.rmtree("gitlab-cloner")

    for project in os.listdir("repos"):
        Popen([
            "gitstats",
            os.path.join("repos", project),
            os.path.join("output", "gitstats", project)
        ]).wait()

        os.chdir(os.path.join("repos", project))
        Popen(["git_stats", "generate"]).wait()
        os.rename(
            "git_stats",
            os.path.join("..", "..", "output", "git_stats", project)
        )

        if os.path.isfile("unittest.sh"):
            Popen(["bash", "unittest.sh"]).wait()
            os.rename(
                "coverage",
                os.path.join("..", "..", "output", "coverage", project)
            )

        if os.path.isfile("docgen.sh"):
            Popen(["bash", "docgen.sh"]).wait()
            os.rename(
                "documentation",
                os.path.join("..", "..", "output", "documentation", project)
            )
            if os.path.isfile("documentation.pdf"):
                os.rename(
                    "documentation.pdf",
                    os.path.join("..", "..", "output", "documentation-pdf",
                                 project + ".pdf")
                )

        os.chdir(os.path.join("..", ".."))


if __name__ == "__main__":
    main()
