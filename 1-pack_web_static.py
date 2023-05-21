#!/usr/bin/python3
"""
Created by Jenaide Sibolie
"""
from fabric.api import *
from datetime import datetime


env.hosts = ['54.162.239.163', '35.153.98.189']
env.user = 'ubuntu'


def do_pack():
    """
    Fabric script that generates a .tgz acrchive from the contents of web_static folder.
    """
    # create the versions folder if it doesn't exists
    local("sudo mkdir -p ./versions")
    now = datetime.now().strftime("%Y%m%d%H%M%S")
    #create the archive
    archive_name = "web_static_{}.tgz".format(now)
    local("sudo tar -czvf {}.tgz web_static".format(archive_name))
    #return the path to the archive if it was created successfully
    name = "{}.tgz".format(archive_name)
    if name:
        return name
    else:
        return None
