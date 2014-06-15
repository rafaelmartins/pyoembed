#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    setup.py
    ~~~~~~~~

    :copyright: (c) 2014 by Rafael Goncalves Martins
    :license: GPL-2, see LICENSE for more details.
"""

from setuptools import setup, find_packages
import os

cwd = os.path.dirname(os.path.abspath(__file__))


setup(
    name='pyoembed',
    version='0.1.1',
    license='BSD',
    description=('A Python library for oEmbed that supports auto-discovered '
                 'and manually included providers.'),
    long_description=open(os.path.join(cwd, 'README.rst')).read(),
    author='Rafael Goncalves Martins',
    author_email='rafael@rafaelmartins.eng.br',
    platforms='any',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'requests',
        'beautifulsoup4',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
    ],
    test_suite='pyoembed.tests',
    tests_require=['mock'],
)
