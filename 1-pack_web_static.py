#!/usr/bin/python3
"""
This module contains a do_pack function
"""

from fabric.api import local
from datetime import datetime

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

if __name__ == "__main__":
    do_pack()
