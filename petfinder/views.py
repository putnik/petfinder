from django.utils.translation import ugettext_lazy as _
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from petfinder.models import *


def home(request):
    petphotos = PetPhoto.objects.select_related()

    city = request.GET['city']
    if (city):
        petphotos = petphotos.filter(pet__city=city)

    kind = request.GET['kind']
    if (kind):
        petphotos = petphotos.filter(pet__kind=kind)

    age = request.GET['age']
    if (age):
        if age == '0-1':
            petphotos = petphotos.filter(pet__age__lte=1)
        elif age == '0-1':
            petphotos = petphotos.filter(pet__age__gte=1, pet__age__lte=3)
        elif age == '3+':
            petphotos = petphotos.filter(pet__age__gte=3)

    sex = request.GET['sex']
    if (sex):
        petphotos = petphotos.filter(pet__sex=sex)

    return render_to_response('home.html', {
        'request':  request,
        'petphotos': petphotos,
        }, context_instance=RequestContext(request))

def pet(request, id):
    pet = PetPhoto.objects.get(id=id)
    photos = PetPhoto.objects.filter(pet=pet)

    return render_to_response('pet.html', {
        'photos': photos,
        }, context_instance=RequestContext(request))

