#!/usr/bin/python3
"""Module to create a tar with Fabric"""

import fabric
import os

# fabric.api.env.hosts = ['35.237.201.94', '35.231.178.196']
# fabric.api.env.user = 'ubuntu'
# fabric.api.env.key_file = '~/.ssh/holberton'
# fabric.api.env.hosts = ['172.31.54.208:45962']
# fabric.api.env.user = 'root'
# fabric.api.env.password = '638f151ec8fd4a571edf'


def do_pack():
    """Generates the tar file"""
    date = fabric.api.local('echo $(date +%Y%m%d%H%M%S)', capture=True)
    fabric.api.local('mkdir -p versions')
    fabric.api.local(
        'tar -cvzf versions/web_static_{}.tgz web_static'.format(date))
    return('versions/web_static_{}.tgz'.format(date))


def do_deploy(archive_path):
    """Distributes archive to web servers"""
    date = archive_path[-18:-4]
    if not os.path.isfile(archive_path):
        return False
    fabric.api.put('versions/web_static_{}.tgz'.format(date), '/tmp/')
    fabric.api.run('mkdir -p /data/web_static/'
                   'releases/web_static_{}/'.format(date))
    fabric.api.run('tar -xzf /tmp/web_static_{}.tgz -C /data/web_static/'
                   'releases/web_static_{}/'.format(date, date))
    fabric.api.run('rm /tmp/web_static_{}.tgz'.format(date))
    fabric.api.run('mv /data/web_static/releases/web_static_{}/'
                   'web_static/* /data/web_static/releases/'
                   'web_static_{}/'.format(date, date))
    fabric.api.run('rm -rf /data/web_static/releases/'
                   'web_static_{}/web_static'.format(date))
    fabric.api.run('rm -rf /data/web_static/current')
    fabric.api.run('ln -s /data/web_static/releases/web_'
                   'static_{}/ /data/web_static/current'.format(date))
    return True


def deploy():
    """Does the same thing as do_delpoy"""
    archive_path = do_pack()
    if not os.path.isfile(archive_path):
        return False
    result = do_deploy(archive_path)
    return result
