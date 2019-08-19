#!/usr/bin/python3
"""Module to create a tar with Fabric"""

import fabric


def do_pack():
    """Generates the tar file"""
    date = fabric.api.local('echo $(date +%Y%m%d%H%M%S)', capture=True)
    fabric.api.local('mkdir -p versions')
    fabric.api.local(
        'tar -cvzf versions/web_static_{}.tgz web_static'.format(date))
    return('versions/web_static_{}.tgz'.format(date))
