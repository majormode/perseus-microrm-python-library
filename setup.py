#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2013 Majormode.
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY,# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import os
import re
import setuptools


EOL_UNIX = '\n'
EOL_WINDOWS = '\r\n'
EOL_MAC = '\r'


def get_author_email():
    """
    Return package email as listed in `__email__` in `init.py`.
    """
    return re.search("^__email__ = ['\"]([^'\"]+)['\"]",
             read_package_init_file(), re.MULTILINE).group(1)


def get_author_name():
    """
    Return package author as listed in `__author__` in `init.py`.
    """
    return re.search("^__author__ = ['\"]([^'\"]+)['\"]",
            read_package_init_file(), re.MULTILINE).group(1)


def get_requirements():
    """
    Return the list of Python libraries that this package depends on.


    @return: a list of the required Python libraries.
    """
    return read_file('requirements.txt') \
        .replace(EOL_WINDOWS, EOL_UNIX) \
        .replace(EOL_MAC, EOL_UNIX) \
        .split(EOL_UNIX)


def get_version():
    """
    Return package version as listed in `__version__` in `init.py`.
    """
    return re.search("^__version__ = ['\"]([^'\"]+)['\"]",
            read_package_init_file(), re.MULTILINE).group(1)


def read_file(file_path_name):
    """
    Read the content of the specified file.


    @param file_path_name: path and name of the file to read.


    @return: content of the specified file.
    """
    with open(os.path.join(os.path.dirname(__file__), file_path_name), 'rt') as fd:
        return fd.read()


def read_package_init_file():
    """
    Read the content of the Python init file of this package.


    @return: the content of the Python init file located at the root of
        this package.
    """
    return read_file('majormode/__init__.py')


setuptools.setup(
    author=get_author_name(),
    author_email=get_author_email(),
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries',
    ],
    description='Python small, little, mini, tiny, micro Object-Relational Mapping (ORM)',
    install_requires=get_requirements(),
    license='MIT',
    long_description=read_file('README.md'),
    long_description_content_type="text/markdown",
    name='majormode-perseus-microrm',
    packages=setuptools.find_packages(),
    platforms = ['any'],
    project_urls={
        'Bug Tracker': 'https://github.com/dcaune/perseus-lib-python-microrm/issues',
        'Documentation': 'https://github.com/dcaune/perseus-lib-python-microrm',
        'Source Code': 'https://github.com/dcaune/perseus-lib-python-microrm',
    },
    version=str(get_version()),
    url='https://github.com/dcaune/perseus-lib-python-microrm',
)
