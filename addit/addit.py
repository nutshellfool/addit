#!/usr/bin/env python

######################################################
#
# addit - instant .gitignore file add helper via the command line
# written by Li Rui (lirui.sep@gmail.com)
# inspired by Benjamin Gleitzman (gleitz@mit.edu)
#
######################################################
import argparse
import requests
import sys
import os

from requests import ConnectionError
from requests.exceptions import SSLError

from . import __version__

FILE_DOWNLOAD_URL = 'https://raw.githubusercontent.com/github/gitignore/master/{0}.gitignore'
SUPPORT_TYPE = ('Java','Python','Objective-C', 'Swift', 'Go')


def get_file_url(param):
    if param not in SUPPORT_TYPE:
        return None
    return FILE_DOWNLOAD_URL.format(param)


def download_file(file_url):
    response = requests.get(file_url, stream=True)
    if response.status_code == 200:
        with open(os.path.join(os.getcwd(), '.gitignore'), 'wb') as f:
            f.write(response.content)
    return response


def _get_instructions(args):
    file_url = get_file_url(args['query'][0])
    if not file_url:
        return False
    response = download_file(file_url)
    return "Add .gitignore file success." if response.status_code == 200 else "download file fail"


def addit(args):
    try:
        return _get_instructions(args) or 'Sorry, couldn\'t find any help with that topic\n'
    except (ConnectionError, SSLError):
        return 'Failed to establish network connection\n'


def get_parser():
    parser = argparse.ArgumentParser(description='instant .gitignore file add helper via the command line')
    parser.add_argument('query', metavar='LANGUAGE', type=str, nargs='*',
                        help='the language of supported in : '+'\t ,'.join(SUPPORT_TYPE))

    parser.add_argument('-v', '--version', help='display current version of addit', action='store_true')
    return parser


def command_performer():
    parser = get_parser()
    args = vars(parser.parse_args())
    if args['version']:
        print(__version__)
        return

    if not args['query']:
        parser.print_help()
        return
    if sys.version < '3':
        print(addit(args).encode('utf-8', 'ignore'))
    else:
        print(addit(args))

if __name__ == '__main__':
    command_performer()
