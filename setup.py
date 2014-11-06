#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
    Author:cleverdeng
    E-mail:clverdeng@gmail.com
    Modified by anakin.yan@gmail.com
"""
from distutils.core import setup

setup(
    name='pinyin',
    version='0.9.1',
    description='hanzi -> pinyin,With Python',
    author='cleverdeng',
    author_email='cleverdeng@gmail.com',
    url='http://github.com/cleverdeng/pinyin.py',
    packages=['pinyin'],
    package_data={'pinyin': ['data/word.data']},
    license='MIT License',
    platforms=['any'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
