#!/usr/bin/python3
"""
a script to generates a .tgz archive
"""
from fabric.api import local
import os
from datetime import datetime


def do_pack():
    """Generates .tgz archive"""

    # versions directory
    if not os.path.exists("versions"):
        os.makedirs("versions")

    # archive path
    now = datetime.now()
    archive_path = "versions/web_static_{}{}{}{}{}{}.tgz".format(
        now.year, now.month, now.day, now.hour, now.minute, now.second)

    # Compressing the static folder
    result = local("tar -cvzf {} web_static".format(archive_path))

    # Checking for success
    if result.failed:
        return None
    else:
        return archive_path
