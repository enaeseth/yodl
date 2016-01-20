#!/usr/bin/env python

import sys
from setuptools import setup, find_packages

requires = ['PyYAML>=3.09']

if sys.version_info[:2] < (2, 7):
    requires.append('ordereddict>=1.1')

setup(
    name='yodl',
    version='1.0.0',
    py_modules=['yodl'],

    url='https://github.com/enaeseth/yodl',
    author='Eric Naeseth',
    author_email='eric+yodl@naeseth.com',

    install_requires=requires,

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ]
)
