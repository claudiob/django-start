# This context processor allows templates to simply access Django settings
# For exaxmple: {% if settings.ENVIRONMENT == 'development' %} {% endif %}
from django.conf import settings as _settings

def settings(request):
    return {'settings': _settings}