from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext 
from models import XXXMODEL_NAMEXXX
from django.conf import settings

def show(request, XXXVAR_NAMEXXX_slug):
    XXXVAR_NAMEXXX = get_object_or_404(XXXMODEL_NAMEXXX, slug=XXXVAR_NAMEXXX_slug)
    return render_to_response('XXXFOLDERXXX/show.html', 
        {'XXXVAR_NAMEXXX': XXXVAR_NAMEXXX}, RequestContext(request))

def index(request):
    XXXVAR_NAMEXXXs = XXXMODEL_NAMEXXX.objects.published()
    return render_to_response('XXXFOLDERXXX/index.html', 
        {'XXXVAR_NAMEXXXs': XXXVAR_NAMEXXXs}, RequestContext(request))
