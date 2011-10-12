# This file will contain
# - a description of this project template
# - the list of variables to be substituted
# - the commands to be launched after copying the template files (e.g. git pull)

# Also, this file will NOT be copied
import os
from random import choice
from string import ascii_lowercase, digits

def after_copy(no_prompt=False):
    """Steps to run after the templates has been copied in place."""
    # 1. Import red-boilerplate in place using git
    os.system("git init")
    os.system("git add .")
    os.system("git commit -m'Django project created with django-start'")
    os.system("git remote add -f boilerplate git://github.com/ff0000/red-boilerplate.git")
    os.system("git pull boilerplate master")
    os.system("git rm README.md")
    os.system("git mv INSTRUCTIONS.md README.md")
    os.system("git commit -m'Restored django-start README.md'")

    # 2. Replace boilerplate variables with prompt values or defaults
    placemarks = [
      ['PROJECT_NAME', 'Project Name', 'Django Project'],
      ['ADMIN_EMAIL',  'Administrator email', 'geeks@ff0000.com'],
    ]
    replace = {}
    for var, help, default in placemarks:
        placemark = '__%s__' % var
        replace[placemark] = None
        while not replace[placemark]:
            if no_prompt:
                replace[placemark] = default
            else:
                prompt = '%s [%s]: ' % (help, default)
                replace[placemark] = raw_input(prompt) or default
    # Also replace SECRET_KEY
    key_seed = ''.join([choice(ascii_lowercase + digits) for x in range(50)])
    replace['__SECRET_KEY_SEED__'] = key_seed

    # WATCH OUT!! This resets permissions!! Change with shutil
    # TODO: Also replace variables in file names
    for root, dirs, files in os.walk('.'):
        DONT_REPLACE_IN = ['.svn', '.git',]
        for folder in DONT_REPLACE_IN:
            if folder in dirs:
                dirs.remove(folder)
        for name in files:
            filepath = os.path.join(root, name)
            with open(filepath, 'r') as f:
                data = f.read()
            for old_val, new_val in replace.items():
                data = data.replace(old_val, new_val)
            with open(filepath, 'w') as f:
                f.write(data)
