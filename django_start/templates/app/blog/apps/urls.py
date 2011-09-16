from django.conf.urls.defaults import *
from models import XXXMODEL_NAMEXXX
from feeds import XXXMODEL_NAMEXXXFeed

urlpatterns = patterns('XXXFOLDERXXX.views',
    (r'^$', 'index', {}, 'XXXVAR_NAMEXXXs'),
    (r'^(?P<XXXVAR_NAMEXXX_slug>.+)/$', 'show', {}, 'XXXVAR_NAMEXXX'),
    (r'^feed/$', XXXMODEL_NAMEXXXFeed(), {}, 'XXXVAR_NAMEXXXs-feed'),
)
