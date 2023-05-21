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


def do_deploy(archive_path):
    """Deploy the boxing package tgz file
    """
    try:
        # Get the filename of the archive
        archive_name = archive_path.split("/")[-1]
        path = '/data/web_static/releases/' + archive.strip(".tgz")
        current = '/data/web_static/current'
        # Upload the archive to the /tmp/ directory of the web server
        put(archive_path, "/tmp/")
        run('mkdir -p {}/'.format(path))
        run('tar -xzf /tmp/{} -C {}'.format(archive_name, path))
        run('rm /tmp/{}'.format(archive_name))
        run('mv {}/web_static/* {}'.format(path, path))
        run('rm -rf {}/web_static'.format(path))
        run('rm -rf {}'.format(current))
        run('ln -s {} {}'.format(path, current))
        print('New version deployed!')
        return True
    except:
        return False


def deploy():
    """
    Function to call do_pack and do_deploy
    """
    archive_path = do_pack()
    call = do_deploy(archive_path)
    return call
