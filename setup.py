from setuptools import setup
import os


README_FILE = open('README')
try:
    LONG_DESCRIPTION = README_FILE.read()
finally:
    README_FILE.close()

ROOT_DIR = os.path.dirname(os.path.realpath(__file__))
DATA_DIR = os.path.join(ROOT_DIR, 'django_start')
STARTPROJECT_DATA = []
for path, dirs, filenames in os.walk(DATA_DIR):
    # Ignore directories that start with '.'
    for i, dir in enumerate(dirs):
        if dir.startswith('.'):
            del dirs[i]
    path = path[len(DATA_DIR) + 1:]
    STARTPROJECT_DATA.append(os.path.join(path, '*.*'))
    # Get files starting with '.' too (they are excluded from the *.* glob).
    STARTPROJECT_DATA.append(os.path.join(path, '.*'))

setup(name='django-start',
      version='0.1.3',
      author='Claudio Baccigalupo',
      author_email='claudio.baccigalupo@ff0000.com',
      description=('Create a Django project based on FF0000 best practices.'),
      url='http://github.com/claudiob/django-start/',
      long_description=LONG_DESCRIPTION,
      packages=['django_start'],
      package_data={'django_start': STARTPROJECT_DATA},
      scripts=['bin/django-start.py'],
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Environment :: Web Environment',
          'Framework :: Django',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Topic :: Software Development :: Libraries :: Python Modules'])
