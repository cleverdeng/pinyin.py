#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
    Author:cleverdeng
    E-mail:clverdeng@gmail.com
"""
from distutils.core import setup
from pinyin import __version__ as version

setup(
            name='pinyin',
            version=version,
            description='hanzi -> pinyin,With Python',
            author='cleverdeng',
            author_email='cleverdeng@gmail.com',
            url='http://github.com/cleverdeng/pinyin.py',
            py_modules=['pinyin'],
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
