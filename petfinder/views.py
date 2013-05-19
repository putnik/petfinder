from django.utils.translation import ugettext_lazy as _
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from petfinder.models import *


def home(request):
    petphotos = PetPhoto.objects.select_related()

    return render_to_response('home.html', {
        'petphotos': petphotos,
        }, context_instance=RequestContext(request))

def pet(request, id):
    pet = PetPhoto.objects.get(id=id)
    photos = PetPhoto.objects.filter(pet=pet)

    return render_to_response('pet.html', {
        'photos': photos,
        }, context_instance=RequestContext(request))

