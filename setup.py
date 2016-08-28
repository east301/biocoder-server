#!/usr/bin/env python3
#
# (c) 2016 biocoder developers
#
# This file is part of biocoder,
# released under Apache License Version 2.0 (http://www.apache.org/licenses/LICENCE).
#

import os
from setuptools import find_packages, setup


# ================================================================================
# helpers
# ================================================================================

def read_requirements(*args):
    here = os.path.join(os.path.dirname(os.path.abspath(__file__)))
    path = os.path.join(here, *args)

    dependencies = []
    with open(path) as fin:
        for line in fin:
            line = line.strip()
            if line and (not line.startswith('#')):
                dependencies.append(line)

    return dependencies


def find_package_data():
    result = {}
    for package in find_packages():
        package_root_path = package.replace('.', os.path.sep)

        package_data = []
        for name in os.listdir(package_root_path):
            if name in ['static', 'templates']:
                package_data.extend(list(enumerate_package_files(package_root_path, name)))

        if package_data:
            result[package] = package_data

    return result


def enumerate_package_files(package_path, search_root_directory_name):
    for root, dirs, files in os.walk(os.path.join(package_path, search_root_directory_name)):
        for name in files:
            yield os.path.relpath(os.path.join(root, name), package_path)


# ================================================================================
# run setup
# ================================================================================

setup(
    # package information
    name='biocoder',
    version='0.0.0',
    description='biocoder',
    long_description='biocoder',
    license='Apache-2.0',
    url='TODO',
    author='east301',
    author_email='me@east301.net',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Django :: 1.9',
        'License :: Other/Proprietary License',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='',

    # package data
    packages=find_packages(),
    package_data=find_package_data(),
    install_requires=read_requirements('requirements-common.txt'),

    # CLI
    entry_points={
        'console_scripts': [
            'biocoder-cli=biocoder.cli:main'
        ]
    }
)
