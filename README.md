# Progstats

|master|develop|
|:---:|:---:|
|[![build status](https://gitlab.namibsun.net/namibsun/python/progstats/badges/master/build.svg)](https://gitlab.namibsun.net/namibsun/python/progstats/commits/master)|[![build status](https://gitlab.namibsun.net/namibsun/python/progstats/badges/develop/build.svg)](https://gitlab.namibsun.net/namibsun/python/progstats/commits/develop)|

![Logo](resources/logo/logo-readme.png)

A Website that categorizes the git statistics, documentation and code coverage
of gitlab projects.

A live version is running at
[progstats.namibsun.net](https://progstats.namibsun.net)

The project is meant to be served using apache and wsgi. The data directory
containing the topics to display should be inside a separate data directory
that is located in the same directory as `progstats.wsgi`. So the structure
of the apache vhost should look something like this:

    /var/www/progstat.namibsun.net/
        -- progstats.wsgi
        -- data/
            -- git_stats/
            -- gitstat/
            ...

An alias to that data directory should also be specified in the
vhost configuration file. A template for a vhost config file is
[here](config/apache.conf)

## Further Information

* [Changelog](CHANGELOG)
* [License (GPLv3)](LICENSE)
* [Gitlab](https://gitlab.namibsun.net/namibsun/python/progstats)
* [Github](https://github.com/namboy94/progstats)
* [Progstats](https://progstats.namibsun.net/projects/progstats)
* [PyPi](https://pypi.org/project/progstats)
