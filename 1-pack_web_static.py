#!/usr/bin/python3
"""A Script to create a .tgz archive in the local machine using fabric api
"""


from fabric.api import *
from datetime import datetime
import os

def do_pack():
    """Method that creates a .tgz archive in the local directory of a codebase
    using operations found in the fabric python module (local)"""
    
    if not os.path.exists('versions'):
        os.makedirs('versions')
    
    now = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = "versions/web_static_{}.tgz".format(now)
    result = local("sudo tar -cvzf {} web_static".format(filename))
    if result.succeeded:
        return filename
    else:
        return None
