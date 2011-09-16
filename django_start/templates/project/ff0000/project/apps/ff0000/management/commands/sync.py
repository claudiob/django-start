# Run python manage.py sync to swipe, synchronize and pre-fill the database

from django.core.management.base import BaseCommand, CommandError
from django.core.management import call_command
import logging
from os import environ

class Command(BaseCommand):
    help = "Swipes, syncs and loads the database with fixtures."

    def handle(self, *args, **options):
        """
        Swipes, syncs and loads the database with fixtures.
        """
        # assume project.settings.ENVIRONMENT else default to 'development'
        env = environ['DJANGO_SETTINGS_MODULE'].split(".")[-1]
        env = 'development' if env == 'settings' else env
        call_command('reset_db')
        call_command('syncdb')
        call_command('loaddata', env)
        logging.info("Sync success")
