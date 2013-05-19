# -*- coding: utf-8 -*-

import urllib, json

from django.utils.translation import ugettext_lazy as _
from django.contrib import admin
from django.conf import settings

from petfinder.models import *


class CityAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('name', 'alias',)
        }),
    )

    list_display = ['name', 'alias',]


class DistrictAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('name', 'alias', 'city',)
        }),
    )

    list_display = ['name', 'alias', 'city',]


class ShelterAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('name', 'city', 'district',)
        }),
    )

    list_display = ['name', 'city',]


class OrgAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('name', 'phone', 'city', 'district', 'description',)
        }),
    )

    list_display = ['name', 'city',]


class PetPhotoInline(admin.TabularInline):
    model = PetPhoto


class PetAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('name', 'kind', 'sex', 'age', 'color', 'health', 'city', 'district', 'description',)
        }),
    )

    list_display = ['name', 'city',]

    inlines = (PetPhotoInline,)


admin.site.register(City, CityAdmin)
admin.site.register(District, DistrictAdmin)
admin.site.register(Shelter, ShelterAdmin)
admin.site.register(Org, OrgAdmin)
admin.site.register(Pet, PetAdmin)

