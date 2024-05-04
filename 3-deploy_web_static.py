#!/usr/bin/python3
"""
This module contains a do_pack function
"""

from fabric.api import local, env, put, run
from datetime import datetime
import os

env.hosts = ["34.232.77.198", "54.237.64.147"]


def do_pack():
    """Creates a .tgz archive from the contents of the web_static folder."""
    try:
        local("mkdir -p versions")

        now = datetime.now()
        timestamp = now.strftime("%Y%m%d%H%M%S")

        archive_name = "versions/web_static_{}.tgz".format(timestamp)
        local("tar -cvzf {} web_static".format(archive_name))

        return archive_name
    except Exception as e:
        print("An error occurred:", e)
        return None


def do_deploy(archive_path):
    """
    This function copies an archive to a web server and unpacks it
    """
    if not os.path.exists(archive_path):
        print("DNE")
        return False

    archive_name = os.path.basename(archive_path)
    release_dir = "/data/web_static/releases/{}"\
        .format(archive_name.split('.')[0])

    put(archive_path, '/tmp/')

    run("sudo mkdir -p {}".format(release_dir))
    run("sudo tar -xzf /tmp/{} -C {}".format(archive_name, release_dir))
    run("sudo rm /tmp/{}".format(archive_name))
    run("sudo mv {}/web_static/* {}".format(release_dir, release_dir))
    run("sudo rm -rf {}/web_static".format(release_dir))
    run("sudo rm -rf /data/web_static/current")
    run("sudo ln -s {} /data/web_static/current".format(release_dir))

    print("New version deployed!")
    return True


def deploy():
    """
    This script packs up an archive using do_pack and
    deploys it using do_deploy
    """
    archive_path = do_pack()
    if archive_path:
        return do_deploy(archive_path)
