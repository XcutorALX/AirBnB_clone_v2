#!/usr/bin/python3
"""
This module contains a do_pack function
"""

from fabric.api import local, env, run, task

env.hosts = ["34.232.77.198", "54.237.64.147"]
env.user = 'ubuntu'
env.key_filename = "~/.ssh/id_rsa"


@task
def do_clean(number=0):
    """
    a Fabric script that deletes out-of-date archives, using the function
    do_clean
    """
    if number == 0:
        number += 1

    local('ls versions/web_static* | head -n -{} | xargs -r rm'.format(number))
    path = '/data/web_static/releases'
    run('find {} -maxdepth 1 -name "web_static_*" -type d | head -n -{} |\
        xargs -r sudo rm -rf'.format(path, number))
