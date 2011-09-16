import os
import sys
from optparse import OptionParser
from django_start.management.base import BaseCommand, CommandError
from django_start.management.importlib import import_module

# A cache of loaded commands, so that call_command doesn't have to reload
_commands = None

def get_commands():
    """
    Returns a dictionary mapping command names to their callback applications.

    The dictionary is cached on the first call and reused on subsequent
    calls.
    """
    global _commands
    if _commands is None:
        command_dir = os.path.join(__path__[0], 'commands')
        try:
            _commands = [f[:-3] for f in os.listdir(command_dir)
                    if not f.startswith('_') and f.endswith('.py')]
        except OSError:
            _commands = []
    return _commands


class ManagementUtility(object):
    """
    Encapsulates the logic of the django-admin.py and manage.py utilities.

    A ManagementUtility has a number of commands, which can be manipulated
    by editing the self.commands dictionary.
    """
    def __init__(self, argv=None):
        self.argv = argv or sys.argv[:]
        self.prog_name = os.path.basename(self.argv[0])

    def main_help_text(self):
        """
        Returns the script's main help text, as a string.
        """
        usage = ['',"Type '%s help <subcommand>' for help on a specific subcommand." % self.prog_name,'']
        usage.append('Available subcommands:')
        commands = get_commands()
        commands.sort()
        for cmd in commands:
            usage.append('  %s' % cmd)
        return '\n'.join(usage)

    def fetch_command(self, subcommand):
        """
        Tries to fetch the given subcommand, printing a message with the
        appropriate command called from the command line if it can't be found.
        """
        if not subcommand in get_commands():
            sys.stderr.write("Unknown command: %r\nType '%s help' for usage.\n" % \
                (subcommand, self.prog_name))
            sys.exit(1)
        module = import_module('django_start.management.commands.%s' % subcommand)
        klass = module.Command()
        return klass

    def execute(self):
        """
        Given the command-line arguments, this figures out which subcommand is
        being run, creates a parser appropriate to that command, and runs it.
        """
        # These options could affect the commands that are available, so they
        # must be processed early.
        parser = OptionParser(usage="%prog subcommand [options] [args]",
                                 option_list=BaseCommand.option_list)
        try:
            options, args = parser.parse_args(self.argv)
        except:
            pass # Ignore any option errors at this point.

        try:
            subcommand = self.argv[1]
        except IndexError:
            subcommand = 'help' # Display help if no arguments were given.

        if subcommand == 'help':
            if len(args) > 2:
                self.fetch_command(args[2]).print_help(self.prog_name, args[2])
            else:
                parser.print_help()
                sys.stderr.write(self.main_help_text() + '\n')
                sys.exit(1)
        elif self.argv[1:] in (['--help'], ['-h']):
            parser.print_help()
            sys.stderr.write(self.main_help_text() + '\n')
        else:
            self.fetch_command(subcommand).run_from_argv(self.argv)


def execute_from_command_line(argv=None):
    """
    A simple method that runs a ManagementUtility.
    """
    utility = ManagementUtility(argv)
    utility.execute()

