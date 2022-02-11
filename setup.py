# -*- coding: utf-8 -*- vim: ts=8 sts=4 sw=4 si et tw=79
from setuptools import setup, find_packages
from os.path import dirname, abspath, join, sep

def read(name):
    fn = join(dirname(abspath(__file__)), name)
    return open(fn, 'r').read()

__author__ = "Tobias Herp <tobias.herp@gmx.de>"
VERSION = (0,
           1,   # initial version
           )
__version__ = '.'.join(map(str, VERSION))

long_description = '\n\n'.join([
    read('README.rst'),
    read('TODO.rst'),
    read('HISTORY.rst'),
    ])

console_scripts = [
        'sort-po = sort_po:main'
        ]

kwargs = {
    'name': 'sort-po',
    'author': 'Tobias Herp',
    'author_email': 'tobias.herp@gmx.de',
    'description': "Sorting tool for Gettext catalogs",
    'long_description': long_description,
    'long_description_content_type': 'text/x-rst',
    'version': __version__,
    'packages': find_packages('src'),
    'install_requires': [
        'setuptools',
        'thebops',
        ],
    'entry_points': {
        'console_scripts': console_scripts,
        },
    'include_package_data': True,
    'license': 'MIT',
    }

setup(**kwargs)
