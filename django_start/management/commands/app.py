import os
from optparse import make_option
from django_start.management.base import BaseCommand, CommandError
from django_start.management.utils import copy_template, camelcase_to_underscore


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

        placemarks = [
            ['MODEL_NAME', 'Model Name', None],
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
        # Now add some placemarks based on other ones
        replace['XXXFOLDERXXX'] = project_folder
        # if MODEL_NAME: BlogPost then VAR_NAME: blog_post
        replace['XXXVAR_NAMEXXX'] = camelcase_to_underscore(replace['XXXMODEL_NAMEXXX'])
        replace['XXXSINGULARXXX'] = replace['XXXVAR_NAMEXXX'].replace('_', ' ')
        replace['XXXPLURALXXX'] = '%ss' % replace['XXXSINGULARXXX']
        copy_template("%s/apps" % src, "apps/%s" % project_folder, replace)
        copy_template("%s/templates" % src, "templates/%s" % project_folder, replace)
        print "Application %s created. To activate:" % replace['XXXMODEL_NAMEXXX']
        print "- Add this line to INSTALLED_APPS in your project settings file:"
        print "\t'%s'," % project_folder
        print "- Add this line to urlpatterns in your project urls file:"
        print "\t(r'^%s/', include('%s.urls'))," % (project_folder, project_folder)
        print "- Synchronize the database"