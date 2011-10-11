# Run python manage.py sync to swipe, synchronize and pre-fill the database

from django.conf import settings
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
        try:
            env = settings.ENVIRONMENT
        except AttributeError:
            env = 'development'
        call_command('reset_db')
        call_command('syncdb')
        call_command('loaddata', env)
        logging.info("Sync success")
