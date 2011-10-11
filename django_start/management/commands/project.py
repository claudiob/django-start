import os, sys
from shutil import copytree, ignore_patterns
from optparse import make_option
from django_start.management.base import BaseCommand, CommandError

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
                no_prompt = options.get('no_prompt', False)
                django_start_settings.after_copy(no_prompt=no_prompt)
            
        