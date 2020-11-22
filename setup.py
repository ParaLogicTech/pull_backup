# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in pull_backup/__init__.py
from pull_backup import __version__ as version

setup(
	name='pull_backup',
	version=version,
	description='Pull backup from another server for replication',
	author='Saif Ur Rehman',
	author_email='saifi0102@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
