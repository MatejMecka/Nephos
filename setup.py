from os import path
from setuptools import setup

# =============================================
# version information

VERSION = (0, 0, 1)
VERSION_SUFFIX = 'under.dev'
VERSION_STRING = ".".join(str(x) for x in VERSION)
RELEASE_STRING = VERSION_STRING + VERSION_SUFFIX

# make changes above when deploying new version
# =============================================


__title__ = "Nephos"
__description__ = "Nephos - Capture stream, process them and upload to cloud storage"
__author__ = "thealphadollar @ CCExtractor"
__author_mail__ = "shivam.cs.iit.kgp@gmail.com"  # TODO: Update author's mail address
__license__ = "GNU GPL v3"
__version__ = VERSION_STRING
__release__ = RELEASE_STRING


def update_version():
    """
    Rewrites version information to `/src/ver_info.py` on every new deployment.

    Returns
    -------

    """
    info = '''# -*- coding: utf-8 -*-

    # =====================================
    # THIS FILE WAS GENERATED AUTOMATICALLY
    # =====================================
    #

    __title__ = '{title}'
    __description__ = '{description}'
    __author__ = '{author}'
    __author_mail = '{author_mail}'
    __license__ = '{license}'
    __version__ = '{version}'
    __release__ = '{release}'
    
    '''.format(
        title=__title__,
        description=__description__,
        author=__author__,
        author_mail=__author_mail__,
        license=__license__,
        version=__version__,
        release=__release__,
    )
    outfile = path.join('src', 'ver_info.py')

    with open(outfile, 'w+', encoding='utf-8') as ver_file:
        ver_file.write(info)


def read(file_name):
    """
    Reads data from file for the description parameter of `setup()`.

    Parameters
    ----------
    file_name: str
        path to the README.md file.

    Returns
    -------
    str
        the text contained in the given file.

    """
    with open(file_name, mode='r') as readme:
        return readme.read()


# update version information before launching setup
update_version()

setup(
    name=__title__,
    version=__version__,
    url="https://github.com/thealphadollar/GSoC18Nephos",
    license=__license__,
    author=__author__,
    author_email=__author_mail__,
    description=__description__,
    long_description=read('README.md'),
    keywords='network stream closed_captions subtitles'
    # TODO: Add package data
    # TODO: Add missing parameters
)