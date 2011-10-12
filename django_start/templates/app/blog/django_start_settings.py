from django_start.management.utils import camelcase_to_underscore

import os
from random import choice
from string import ascii_lowercase, digits

def after_copy(project_folder, no_prompt=False):
    """Steps to run after the app template has been copied in place."""

    # 2. Replace boilerplate variables with prompt values or defaults
    placemarks = [
      ['MODEL_NAME', 'Model Name', 'Post'],
    ]
    replace = {}
    for var, help, default in placemarks:
        placemark = 'XXX%sXXX' % var
        replace[placemark] = None
        while not replace[placemark]:
            if no_prompt:
                replace[placemark] = default
            else:
                prompt = '%s [%s]: ' % (help, default)
                replace[placemark] = raw_input(prompt) or default
    # OPTIMIZE: Automate the following replacements
    # See https://github.com/ff0000/django-start/issues/2
    # Now add some placemarks based on other ones
    replace['XXXFOLDERXXX'] = project_folder
    # if MODEL_NAME: BlogPost then VAR_NAME: blog_post
    replace['XXXVAR_NAMEXXX'] = camelcase_to_underscore(replace['XXXMODEL_NAMEXXX'])
    replace['XXXSINGULARXXX'] = replace['XXXVAR_NAMEXXX'].replace('_', ' ')
    replace['XXXPLURALXXX'] = '%ss' % replace['XXXSINGULARXXX']

    # WATCH OUT!! This resets permissions!! Change with shutil

    # OPTIMIZE: Shouldn't need to loop in two folders
    # os.chdir(os.path.abspath(project_folder))
    for folder in ['apps', 'templates']:
        subfolder = os.path.join(folder, project_folder)

        for root, dirs, files in os.walk(subfolder):
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

    # TODO: Automate the following
    print "Application %s created. To activate:" % replace['XXXMODEL_NAMEXXX']
    print "1. Add this line to INSTALLED_APPS in your project settings file:"
    print "\t'%s'," % project_folder
    print "2. Add this line to urlpatterns in your project urls file:"
    print "\t(r'^%s/', include('%s.urls'))," % (project_folder, project_folder)
    print "3. Synchronize the database"
