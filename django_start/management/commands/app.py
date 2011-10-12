import os, sys
from shutil import copytree, ignore_patterns
from optparse import make_option
from django_start.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    help = """
        Create a Django app from a template, replacing boilerplate variables.
        Also adds the app to INSTALLED_APPS and register its urls."""
    args = "[project_folder]"

    TEMPLATE_DIR = os.path.join(os.path.dirname(__file__), 
        '..', '..', 'templates', 'app', 'blog')

    option_list = BaseCommand.option_list + (
        make_option('--template-dir', action='store', default=TEMPLATE_DIR, 
            help='Project template directory to use.'),)


    def handle(self, *args, **options):
        if len(args) != 1:
            raise CommandError('Indicate the folder name for the app.')
        no_prompt = options.get('no_prompt', False)
        app_dir = options['template_dir']
        project_folder = args[0]
        # 1. Copy the <name>/apps into apps/<name>
        copy_from = os.path.join(app_dir, 'apps')
        copy_to = os.path.join('apps', project_folder)
        copytree(copy_from, copy_to)
        # 1. Copy the <name>/templates into templates/<name>
        copy_from = os.path.join(app_dir, 'templates')
        copy_to = os.path.join('templates', project_folder)
        copytree(copy_from, copy_to)
        # 2. If template has a settings file, run its after_copy method
        settings_path = os.path.join(app_dir, 'django_start_settings.py')
        if os.path.exists(settings_path):
            sys.path.append(app_dir)
            import django_start_settings
            if callable(getattr(django_start_settings, 'after_copy', None)):
                # Don't change current directory (there are two in this case)
                django_start_settings.after_copy(no_prompt=no_prompt,
                    project_folder=project_folder)
