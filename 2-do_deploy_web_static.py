#!/usr/bin/python3
"""
distributes an archive to your web servers, using the function do_deploy
"""

from fabric.api import env, put, run
import os


env.hosts = ["34.232.77.198", "54.237.64.147"]

def do_deploy(archive_path):
    """
    This function copies an archive to a web server and unpacks it
    """
    if not os.path.exists(archive_path):
        print("DNE")
        return False

    archive_name = os.path.basename(archive_path)
    release_dir = "/data/web_static/releases/{}".format(archive_name.split('.')[0])

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
