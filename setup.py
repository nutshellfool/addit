#!/usr/bin/env python

from setuptools import setup, find_packages
import addit
import os


def extra_dependencies():
    import sys
    ret = []
    if sys.version_info < (2, 7):
        ret.append('argparse')
    return ret


def read(*names):
    values = dict()
    extensions = ['.txt', '.rst']
    for name in names:
        value = ''
        for extension in extensions:
            filename = name + extension
            if os.path.isfile(filename):
                value = open(name + extension).read()
                break
        values[name] = value
    return values


long_description = """

%(README)s
News
====
%(CHANGES)s
""" % read('README', 'CHANGES')

setup(
    name='addit',
    version=addit.__version__,
    description='Instant add .gitignore file via the command line',
    long_description='Add the .gitignore file via command line',
    keywords='addit help console command line gitignore',
    author='Richard Li',
    author_email='lirui.sep@gmail.com',
    maintainer='Richard Li',
    maintainer_email='lirui.sep@gmail.com',
    url='https://github.com/nutshellfool/addit',
    license='MIT',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'addit = addit.addit:command_performer',
        ]
    },
    install_requires=[
        'requests',
    ] + extra_dependencies(),
    python_requires='>=3.5',
)