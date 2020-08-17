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

from progstats.router import app
from cheroot.wsgi import Server, PathInfoDispatcher


def main():
    server = Server(
        ("0.0.0.0", 8000),
        PathInfoDispatcher({"/": app})
    )
    server.start()


if __name__ == "__main__":
    main()
