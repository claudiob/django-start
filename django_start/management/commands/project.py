import os, sys
from shutil import copytree, ignore_patterns
from optparse import make_option
from django_start.management.base import BaseCommand, CommandError

def copy_template_folder(copy_from, copy_to, exclude=[]):
    """Copy all files in the source path to the destination path."""
    for copy_from, dirs, files in os.walk(copy_from):
        relative_path = copy_from[len(copy_from):].lstrip(os.sep)
        for filename in files:
            if filename in exclude:
                continue
            src_file_path = os.path.join(copy_from, filename)
            dest_file_path = os.path.join(copy_to, relative_path, filename)
            copy_template_file(src_file_path, dest_file_path)

def copy_template_file(src, dest):
    """Copy a file, maintaining its permissions."""
    if not os.path.exists(os.path.dirname(dest)):
        os.makedirs(os.path.dirname(dest))
    with open(src, 'r') as src_file:
        with open(dest, 'w') as dest_file:
            dest_file.write(src_file.read())
    shutil.copymode(src, dest)


class Command(BaseCommand):
    help = """Create a Django project from a template.
    
    The template must include a file called `django_start.py` that contains
    the documentation for the template, the optional boilerplate variables
    to substitute with prompt values and the actions to perform after having
    copied the template files (e.g., importing more files with git)."""

    args = "[project_folder]"

    TEMPLATE_DIR = os.path.join(os.path.dirname(__file__), 
        '..', '..', 'templates', 'project', 'ff0000')

    option_list = BaseCommand.option_list + (make_option('--template-dir', 
        action='store', default=TEMPLATE_DIR, help='Project template to use'),)

    def handle(self, *args, **options):
        if len(args) != 1:
            raise CommandError('Indicate the folder name for the project.')
        # 1. Copy the template folder
        copy_from = options['template_dir']
        copy_to = args[0]
        copytree(copy_from, copy_to, ignore=ignore_patterns('django_start*',))
        # 2. If template has a settings file, run its after_copy method
        settings_path = os.path.join(copy_from, 'django_start_settings.py')
        if os.path.exists(settings_path):
            sys.path.append(copy_from)
            import django_start_settings
            if callable(getattr(django_start_settings, 'after_copy', None)):
                # First change current directory to copy_to
                os.chdir(copy_to)
                django_start_settings.after_copy()
            
        