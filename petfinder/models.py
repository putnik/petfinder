import os.path

from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.core.files.images import ImageFile


class City(models.Model):
    name = models.CharField(max_length=50, verbose_name=_("Name"))
    alias = models.CharField(max_length=50, verbose_name=_("Alias"))

    class Meta:
        ordering = ['name',]

    def __unicode__(self):
        return self.name


class District(models.Model):
    name = models.CharField(max_length=50, verbose_name=_("Name"))
    alias = models.CharField(max_length=50, verbose_name=_("Alias"))
    city = models.ForeignKey('City', verbose_name=_("City"))

    class Meta:
        ordering = ['city', 'name',]

    def __unicode__(self):
        return self.name


class Pet(models.Model):
    KIND_CHOICES = (
        ('C', _("Cat")),
        ('D', _("Dog")),
        ('O', _("Other")),
    )

    SEX_CHOICES = (
        ('M', _("Male")),
        ('F', _("Female")),
    )

    SEX_CHOICES = (
        ('M', _("Male")),
        ('F', _("Female")),
    )

    SIZE_CHOICES = (
        ('S', _("Small")),
        ('M', _("Medium")),
        ('L', _("Large")),
    )

    HEALTH_CHOICES = (
        ('G', _("Good")),
        ('C', _("Common")),
        ('B', _("Bad")),
    )

    name = models.CharField(max_length=250, verbose_name=_("Name"))
    kind = models.CharField(max_length=1, choices=KIND_CHOICES, default='O', verbose_name=_("Kind"))
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, verbose_name=_("Sex"))
    age = models.IntegerField(verbose_name=_("Age"))
    color = models.CharField(max_length=100, verbose_name=_("Color"))
    size = models.CharField(max_length=1, choices=SIZE_CHOICES, verbose_name=_("Size"))
    health = models.CharField(max_length=1, choices=HEALTH_CHOICES, verbose_name=_("Health"))
    description = models.TextField(blank=True, verbose_name=_("Description"))
    city = models.ForeignKey('City', verbose_name=_("City"))
    district = models.ForeignKey('District', blank=True, verbose_name=_("District"))

    class Meta:
        ordering = ['name',]

    def __unicode__(self):
        return self.name


class PetPhoto(models.Model):
    def make_upload_folder(instance, filename):
        dir_name, image_name = os.path.split(filename)
        path = u"%d/%s" % (instance.pet.pk, image_name)
        return path

    pet = models.ForeignKey('Pet', verbose_name=_("Pet"))
    file = models.FileField(upload_to=make_upload_folder)
    title = models.CharField(max_length=250, blank=True, verbose_name=_("Title"))

    def __unicode__(self):
        return self.title


class Org(models.Model):
    name = models.CharField(max_length=250, verbose_name=_("Name"))
    phone = models.CharField(max_length=50, verbose_name=_("Phone"))
    description = models.TextField(blank=True, verbose_name=_("Description"))
    city = models.ForeignKey('City', verbose_name=_("City"))
    district = models.ForeignKey('District', blank=True, verbose_name=_("District"))

    class Meta:
        ordering = ['name',]

    def __unicode__(self):
        return self.name

