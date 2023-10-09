#!/usr/bin/python3
# Fabric script that generates a .tgz archive from the contents of the web_static

from fabric.api import local
from datetime import datetime
import os

def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder.
    """
    try:
        # Create the 'versions' folder if it doesn't exist
        if not os.path.exists('versions'):
            os.makedirs('versions')

        # Create the archive name using the current timestamp
        now = datetime.now()
        archive_name = "web_static_{}{}{}{}{}{}.tgz".format(
            now.year, now.month, now.day, now.hour, now.minute, now.second
        )

        # Compress the contents of the 'web_static' folder into the archive
        local("tar -czvf versions/{} web_static".format(archive_name))

        # Return the archive path if the archive has been generated successfully
        return "versions/{}".format(archive_name)
    except Exception as e:
        return None

if __name__ == "__main__":
    result = do_pack()
    if result:
        print("Archive created: {}".format(result))
    else:
        print("Archive creation failed.")
