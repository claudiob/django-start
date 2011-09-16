# Run python manage.py dump to dump a model's data into a fixture

from django.core.management.base import BaseCommand, CommandError
import logging
from os import system, environ        

class Command(BaseCommand):
    help = "Dump a model's data into a fixture."

    def handle(self, *args, **options):
        """
        Dump a model's data into a fixture.
        Uses --natural to avoid writing content_type_id which are subject
        to changes while an application is under development.
        Example: python manage.py pictures
        """
        # assume project.settings.ENVIRONMENT else default to 'development'
        env = environ['DJANGO_SETTINGS_MODULE'].split(".")[-1]
        env = 'development' if env == 'settings' else env
        # TODO: Raise error if the parameter is not passed
        model = args[0] 
        options = " --indent=4 --natural"
        output = "apps/%s/fixtures/%s.json" % (model, env)
        system('python manage.py dumpdata %s %s > %s' % 
            (model, options, output))
        logging.info("Dump success")
