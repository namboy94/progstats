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

if [ "$#" -ne 2 ]; then
    echo "Usage: backup.sh <backup-file> <backup_data>"
    exit 1
fi

APP_CONTAINER="progstats-app"
CONTENT_VOLUME="progstats_content"
SSH_CONFIG_VOLUME="progstats_ssh_config"
TARGET=$1

rm -rf backup
mkdir backup

docker-compose up -d --no-recreate
docker run --rm -v "$SSH_CONFIG_VOLUME":/ssh_config -v "$(pwd)"/backup:/target \
    ubuntu tar -zcvpf /target/ssh_config.tar.gz /ssh_config

if [ "$2" == 1 ]; then
    echo "Backing up data"
    docker run --rm -v "$CONTENT_VOLUME":/content -v "$(pwd)"/backup:/target \
      ubuntu tar -zcvpf /target/content.tar.gz /content;
else
    mkdir empty
    docker run --rm -v "$(pwd)/empty":/content -v "$(pwd)"/backup:/target \
      ubuntu tar -zcvpf /target/content.tar.gz /content;
    rmdir empty
fi



docker exec -it "$APP_CONTAINER" printenv > backup/.env

tar -zcvpf "$TARGET" backup
rm -rf backup
