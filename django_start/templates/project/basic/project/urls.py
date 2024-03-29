from django.conf import settings
from django.conf.urls.defaults import *
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView

admin.autodiscover()
urlpatterns = patterns('',
    (r'^grappelli/', include('grappelli.urls')),
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
    # Homepage
    (r'^$', TemplateView.as_view(template_name='homepage.html')),
)

# Static URLs
urlpatterns += staticfiles_urlpatterns()

# Static admin URLs
urlpatterns.insert(-2, url(r'^%s(?P<path>.*)' % settings.ADMIN_MEDIA_PREFIX[1:],
    'django.views.static.serve', {'document_root': settings.ADMIN_MEDIA_ROOT}))

# Upload URLS
if settings.DEBUG:
    urlpatterns.insert(-2, url(r'^%s(?P<path>.*)' % settings.MEDIA_URL[1:],
        'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}))
