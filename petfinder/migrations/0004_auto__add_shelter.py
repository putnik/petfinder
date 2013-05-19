# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Shelter'
        db.create_table(u'petfinder_shelter', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('city', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['petfinder.City'])),
            ('district', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['petfinder.District'], blank=True)),
        ))
        db.send_create_signal(u'petfinder', ['Shelter'])


    def backwards(self, orm):
        # Deleting model 'Shelter'
        db.delete_table(u'petfinder_shelter')


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
            'location': ('django.db.models.fields.CharField', [], {'default': "'H'", 'max_length': '1'}),
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
        },
        u'petfinder.shelter': {
            'Meta': {'ordering': "['city', 'name']", 'object_name': 'Shelter'},
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['petfinder.City']"}),
            'district': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['petfinder.District']", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['petfinder']