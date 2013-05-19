# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Pet.breed'
        db.add_column(u'petfinder_pet', 'breed',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Pet.breed'
        db.delete_column(u'petfinder_pet', 'breed')


    models = {
        u'petfinder.city': {
            'Meta': {'ordering': "['name']", 'object_name': 'City'},
            'alias': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'petfinder.district': {
            'Meta': {'ordering': "['city', 'name']", 'object_name': 'District'},
            'alias': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['petfinder.City']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'petfinder.org': {
            'Meta': {'ordering': "['name']", 'object_name': 'Org'},
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['petfinder.City']"}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'district': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['petfinder.District']", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'petfinder.pet': {
            'Meta': {'ordering': "['name']", 'object_name': 'Pet'},
            'age': ('django.db.models.fields.IntegerField', [], {}),
            'breed': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['petfinder.City']"}),
            'color': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'district': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['petfinder.District']", 'blank': 'True'}),
            'health': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kind': ('django.db.models.fields.CharField', [], {'default': "'O'", 'max_length': '1'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'sex': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'size': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        },
        u'petfinder.petphoto': {
            'Meta': {'object_name': 'PetPhoto'},
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pet': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['petfinder.Pet']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'})
        }
    }

    complete_apps = ['petfinder']