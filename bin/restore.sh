#!/bin/bash
# Copyright 2018 Hermann Krumrey <hermann@krumreyh.com>
#
# This file is part of progstats.
#
# progstats is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# progstats is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with progstats.  If not, see <http://www.gnu.org/licenses/>.

set -e

if [ "$#" -ne 1 ]; then
    echo "Usage: restore.sh <backup-file>"
    exit 1
fi

CONTENT_VOLUME="progstats_content"
SSH_CONFIG_VOLUME="progstats_ssh_config"
TARGET=$1

rm -rf backup .env
tar xvf "$TARGET"
cp backup/.env .env

docker-compose up --no-start

docker run -i --rm -v "$CONTENT_VOLUME":/content -v "$(pwd)"/backup:/target \
    ubuntu bash -c 'rm -rf /content/* && tar -C / -xvf /target/content.tar.gz'
docker run -i --rm -v "$SSH_CONFIG_VOLUME":/ssh_config -v "$(pwd)"/backup:/target \
    ubuntu bash -c 'rm -rf /ssh_config/* && tar -C / -xvf /target/ssh_config.tar.gz'

docker-compose up -d

rm -rf backup
