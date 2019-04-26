#!/usr/bin/env python

import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
	README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
	name='aaisp',
	version='0.4',
	packages=find_packages(),
	include_package_data=True,
	long_description=README,
	install_requires=[
		'requests',
	],
)
