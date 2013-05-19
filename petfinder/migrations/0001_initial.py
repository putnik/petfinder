# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'City'
        db.create_table(u'petfinder_city', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('alias', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'petfinder', ['City'])

        # Adding model 'District'
        db.create_table(u'petfinder_district', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('alias', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('city', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['petfinder.City'])),
        ))
        db.send_create_signal(u'petfinder', ['District'])

        # Adding model 'Pet'
        db.create_table(u'petfinder_pet', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('kind', self.gf('django.db.models.fields.CharField')(default='O', max_length=1)),
            ('sex', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('age', self.gf('django.db.models.fields.IntegerField')()),
            ('color', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('size', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('health', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('city', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['petfinder.City'])),
            ('district', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['petfinder.District'], blank=True)),
        ))
        db.send_create_signal(u'petfinder', ['Pet'])

        # Adding model 'PetPhoto'
        db.create_table(u'petfinder_petphoto', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('pet', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['petfinder.Pet'])),
            ('file', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=250, blank=True)),
        ))
        db.send_create_signal(u'petfinder', ['PetPhoto'])

        # Adding model 'Org'
        db.create_table(u'petfinder_org', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('city', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['petfinder.City'])),
            ('district', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['petfinder.District'], blank=True)),
        ))
        db.send_create_signal(u'petfinder', ['Org'])


    def backwards(self, orm):
        # Deleting model 'City'
        db.delete_table(u'petfinder_city')

        # Deleting model 'District'
        db.delete_table(u'petfinder_district')

        # Deleting model 'Pet'
        db.delete_table(u'petfinder_pet')

        # Deleting model 'PetPhoto'
        db.delete_table(u'petfinder_petphoto')

        # Deleting model 'Org'
        db.delete_table(u'petfinder_org')


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
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['petfinder.City']"}),
            'color': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
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