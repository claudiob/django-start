import os
import re
import shutil
import stat
from random import choice

def camelcase_to_underscore(name):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

def copy_template(src, dest, replace=None):
    """
    Copy all files in the source path to the destination path.
    
    To replace boilerplate strings in the source data, pass a dictionary to the
    ``replace`` argument where each key is the boilerplate string and the
    corresponding value is the string which should replace it.
    
    The destination file paths are also parsed through the boilerplate
    replacements, so directories and file names may also be modified.
    
    """
    for path, dirs, files in os.walk(src):
        relative_path = path[len(src):].lstrip(os.sep)
        # Replace boilerplate strings in destination directory.
        for old_val, new_val in replace.items():
            relative_path = relative_path.replace(old_val, new_val)
        try:
            os.mkdir(os.path.join(dest, relative_path))
        except:
            # TODO: remove this
            pass
        for i, subdir in enumerate(dirs):
            if subdir.startswith('.'):
                del dirs[i]
        for filename in files:
            if (filename.startswith('djangostart') or
                filename.endswith('.pyc')):
                continue
            src_file_path = os.path.join(path, filename)
            # Replace boilerplate strings in destination filename.
            for old_val, new_val in replace.items():
                filename = filename.replace(old_val, new_val)
            dest_file_path = os.path.join(dest, relative_path, filename)
            copy_template_file(src_file_path, dest_file_path, replace)


def copy_template_file(src, dest, replace=None):
    """
    Copy a source file to a new destination file, maintaining its permissions.
    
    To replace boilerplate strings in the source data, pass a dictionary to the
    ``replace`` argument where each key is the boilerplate string and the
    corresponding value is the string which should replace it.
    
    """
    replace = replace or {}
    # Read the data from the source file.
    src_file = open(src, 'r')
    data = src_file.read()
    src_file.close()
    # Replace boilerplate strings.
    for old_val, new_val in replace.items():
        data = data.replace(old_val, new_val)

    # Generate SECRET_KEY for settings file
    secret_key = ''.join([choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)') for i in range(50)])
    data = re.sub(r"(?<=SECRET_KEY = ')'", secret_key + "'", data)

    # Create the folder if it does not exist
    dest_folder = os.path.dirname(dest)
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    # Write the data to the destination file.
    dest_file = open(dest, 'w')
    dest_file.write(data)
    dest_file.close()
    # Copy permissions from source file.
    shutil.copymode(src, dest)
    # Make new file writable.
    if os.access(dest, os.W_OK):
        st = os.stat(dest)
        new_permissions = stat.S_IMODE(st.st_mode) | stat.S_IWUSR
        # TODO: Remove this from here, should be managed by setuptoold
        # Make manage.py executable again:
        if os.path.basename(dest) == 'manage.py':
            new_permissions |= stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH
        os.chmod(dest, new_permissions)

