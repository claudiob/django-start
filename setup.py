#!/usr/bin/env python
# -*- coding: utf-8 -*-
try:
    from setuptools import setup
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup

setup(
    name='django-start',
    version='0.1.9',
    description='Create a Django project based on FF0000 best practices.',
    author='RED Interactive Agency',
    author_email='claudio.baccigalupo@ff0000.com',
    url='http://github.com/ff0000/django-start/',
    packages=[
        'django_start',
        'django_start.management',
    ],
    # Note: Using MANIFEST.in instead of package_data, as it is respected
    # both by bdist and sdist, see http://stackoverflow.com/questions/6714145/
    include_package_data=True,
    exclude_package_data = { '': ['*.pyc', '.DS_Store'] },
    scripts=['bin/django-start.py'],
    classifiers=[
          'Development Status :: 3 - Alpha',
          'Environment :: Web Environment',
          'Framework :: Django',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Topic :: Utilities'
    ]
)
