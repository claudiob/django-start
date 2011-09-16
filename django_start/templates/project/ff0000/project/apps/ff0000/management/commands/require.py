# Run python manage.py require to load the requirements in a given environment

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
import logging
from os import system, environ        

class Command(BaseCommand):
    help = "Install the python requirements for a given environment."
    can_import_settings = False
    requires_model_validation = False
    def handle(self, *args, **options):
        """
        Install the python requirements for a given environment.
        """
        # assume project.settings.ENVIRONMENT else default to 'development'
        env = environ['DJANGO_SETTINGS_MODULE'].split(".")[-1]
        env = 'development' if env == 'settings' else env
        system('pip install -r ../deploy/requirements/base.txt')
        system('pip install -r ../deploy/requirements/%s.txt' % env)
        logging.info("Require success")
