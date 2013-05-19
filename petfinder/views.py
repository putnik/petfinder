from django.utils.translation import ugettext_lazy as _
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from petfinder.models import *


def search(request):
    pets = Pet.objects.extra(
        select={
            'photo': '''
                SELECT file
                FROM petfinder_petphoto
                WHERE petfinder_petphoto.pet_id = petfinder_pet.id
                LIMIT 1
            '''
        },
    )

    if ('city' in request.GET and request.GET['city']):
        pets = pets.filter(city=request.GET['city'])

    if ('kind' in request.GET and request.GET['kind']):
        pets = pets.filter(kind=request.GET['kind'])

    if ('age' in request.GET and request.GET['age']):
        if request.GET['age'] == '0-1':
            pets = pets.filter(age__lte=1)
        elif request.GET['age'] == '0-1':
            pets = pets.filter(age__gte=1, age__lte=3)
        elif request.GET['age'] == '3+':
            pets = pets.filter(age__gte=3)

    if ('sex' in request.GET and request.GET['sex']):
        pets = pets.filter(sex=request.GET['sex'])

    return render_to_response('search.html', {
        'request': request,
        'pets': pets,
        }, context_instance=RequestContext(request))

def pet(request, id):
    pet = Pet.objects.get(id=id)
    photos = PetPhoto.objects.filter(pet=pet)

    if 0 in photos:
        photo = photos[0]
    else:
        photo = None

    return render_to_response('pet.html', {
        'pet': pet,
        'photo': photo,
        'photos': photos[1:5],
        }, context_instance=RequestContext(request))

