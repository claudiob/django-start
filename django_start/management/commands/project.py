import os
from optparse import make_option
from django_start.management.base import BaseCommand, CommandError
from django_start.management.utils import copy_template


class Command(BaseCommand):
    help = """
        Create a Django project from a template, replacing boilerplate 
        variables."""
    args = "[project_folder]"

    TEMPLATE_DIR = os.path.join(os.path.dirname(__file__), 
        '..', '..', 'templates', 'project', 'ff0000')

    option_list = BaseCommand.option_list + (
        make_option('--template-dir', action='store', default=TEMPLATE_DIR, 
            help='Project template directory to use.'),)

    def handle(self, *args, **options):
        if len(args) != 1:
            raise CommandError('Indicate the folder name for the project.')

        placemarks = [
            ['PROJECT_NAME', 'Project Name', 'Django Project'],
            ['ADMIN_EMAIL', 'Administrator email', 'geeks@ff0000.com'],
            ['GOOGLE_SITE_VERIFICATION', 'Google site verification code', 
                'Check http://www.google.com/webmasters/'],
            ['GOOGLE_ANALYTICS_CODE', 'Google Analytics code', 'UA-XXXXXXXX'],
        ]

        src = options['template_dir']
        project_folder = args[0]
        replace = {}
        for var, help, default in placemarks:
            placemark = 'XXX%sXXX' % var
            replace[placemark] = None
            while not replace[placemark]:
                prompt = '%s [%s]: ' % (help, default)
                replace[placemark] = raw_input(prompt) or default
        copy_template(src, project_folder, replace)
