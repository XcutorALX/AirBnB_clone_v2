#!/usr/bin/python3
"""
distributes an archive to your web servers, using the function do_deploy
"""

from fabric.api import env, put, run
import os


env.hosts = ["34.232.77.198", "54.237.64.147"]
env.user = "ubuntu"
env.key_filename = "~/.ssh/id_rda"

def do_deploy(archive_path):
    if not os.path.exists(archive_path):
        return False

    try:
        archive_name = os.path.basename(archive_path)
        release_dir = "/data/web_static/releases/{}".format(archive_name.split('.')[0])

        put(archive_path, '/tmp/')

        run("sudo mkdir -p {}".format(release_dir))
        run("sudo tar -xzf /tmp/{} -C {}".format(archive_name, release_dir))
        run("sudo rm /tmp/{}".format(archive_name))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s {} /data/web_static/current".format(release_dir))

        return True
    except Exception as e:
        return False
