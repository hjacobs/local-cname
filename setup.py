#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import find_packages, setup


def readme():
    try:
        return open('README.rst', encoding='utf-8').read()
    except TypeError:
        return open('README.rst').read()


setup(
    name='local-cname',
    packages=find_packages(),
    version='0.3',
    description='Helper script to emulate a local CNAME DNS by writing to /etc/hosts',
    long_description=readme(),
    author='henning@jacobs1.de',
    url='https://github.com/hjacobs/local-cname',
    keywords='dns hosts local',
    license='GNU General Public License v3 (GPLv3)',
    setup_requires=['flake8'],
    install_requires=['clickclick', 'filelock'],
    tests_require=[],
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Intended Audience :: Developers',
        'Development Status :: 3 - Alpha',
        'Operating System :: POSIX',
    ],
    entry_points={'console_scripts': ['local-cname = local_cname.cli:main']}
)
