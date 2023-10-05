#!/usr/bin/python3
# Fabric script that generates a .tgz archive from the contents of the web_static

import os.path
from datetime import datetime
from fabric.api import local

def do_pack():
    """Create a tar gzipped archive of the directory web_static."""

    # Get the current timestamp
    dtime = datetime.utcnow()

    # Define the archive file name with the current timestamp
    file = "versions/web_static_{}{}{}{}{}{}.tgz".format(
    dtime.year, dtime.month, dtime.day, dtime.hour, dtime.minute, dtime.second)

    # Check if the 'versions' directory exists; if not, create it
    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None

    # Create the .tgz archive from the 'web_static' directory
    if local("tar -cvzf {} web_static".format(file)).failed is True:
        return None

    # Return the path to the created archive
    return file
