# Fabric script that generates a .tgz archive from the contents of the web_static

from fabric.api import local
from datetime import datetime

def do_pack():
    """
    This generates a .tgz archive from the contents of the web_static folder.
    """
    try:
        now = datetime.now()
        archive_name = "web_static_{}{}{}{}{}{}.tgz".format(
            now.year, now.month, now.day, now.hour, now.minute, now.second)
        archive_path = "versions/{}".format(archive_name)

        local("mkdir -p versions")
        local("tar -cvzf {} web_static".format(archive_path))

        return archive_path
    except Exception:
        return None
