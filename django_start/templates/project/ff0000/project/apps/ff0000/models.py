import os
import sys
from django.conf import settings

# Prevent interactive question about wanting a superuser created
# since the admin user is already created through the initial data
# (taken from http://stackoverflow.com/questions/1466827/)
from django.db.models import signals
from django.contrib.auth.management import create_superuser
from django.contrib.auth import models as auth_app
signals.post_syncdb.disconnect(create_superuser, sender=auth_app,
    dispatch_uid = "django.contrib.auth.management.create_superuser")

if settings.DEBUG:
    # Load host-specific configuration file from hosts/[hostname].py
    from socket import gethostname # Hostname based local settings 
    hostname = gethostname().split('.')[0]
    try:
        _f = __file__              
        path = os.path.join(settings.PROJECT_ROOT, 'settings')
        sys.path.insert(0, path)   
        globals().update(__import__(hostname).__dict__)
        sys.path.remove(path)      
        __file__ = _f              
    except ImportError, e: 
        print >> sys.stderr, '[33mLocal settings file: [[34msettings/%s.py[33m] error:[0m\n%s' % (hostname,e)
