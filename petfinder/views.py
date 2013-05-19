from django.utils.translation import ugettext_lazy as _
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from petfinder.models import *


def home(request):
    petphotos = PetPhoto.objects.select_related()

    if ('city' in request.GET and request.GET['city']):
        petphotos = petphotos.filter(pet__city=request.GET['city'])

    if ('kind' in request.GET and request.GET['kind']):
        petphotos = petphotos.filter(pet__kind=request.GET['kind'])

    if ('age' in request.GET and request.GET['age']):
        if request.GET['age'] == '0-1':
            petphotos = petphotos.filter(pet__age__lte=1)
        elif request.GET['age'] == '0-1':
            petphotos = petphotos.filter(pet__age__gte=1, pet__age__lte=3)
        elif request.GET['age'] == '3+':
            petphotos = petphotos.filter(pet__age__gte=3)

    if ('sex' in request.GET and request.GET['sex']):
        petphotos = petphotos.filter(pet__sex=request.GET['sex'])

    return render_to_response('search.html', {
        'request':  request,
        'petphotos': petphotos,
        }, context_instance=RequestContext(request))

def pet(request, id):
    pet = Pet.objects.get(id=id)
    photos = PetPhoto.objects.filter(pet=pet)

    return render_to_response('pet.html', {
        'pet': pet,
        'photo': photos[0],
        'photos': photos[1:5],
        }, context_instance=RequestContext(request))

