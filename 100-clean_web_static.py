#!/usr/bin/python3
"""
Removing out-of-date archives
"""
from fabric.api import *
import os

env.hosts = ['100.27.4.8', '18.207.1.51']


def do_clean(number=0):
    """
    deleting expired archives
    """
    number = 1 if int(number) == 0 else int(number)

    archives = sorted(os.listdir("versions"))
    [archives.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archives]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        [archives.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in archives]
