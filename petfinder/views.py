from django.utils.translation import ugettext_lazy as _
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from petfinder.models import *


def home(request):
    return render_to_response('home.html', {
        }, context_instance=RequestContext(request))



