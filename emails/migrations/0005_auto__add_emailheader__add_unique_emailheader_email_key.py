# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'EmailHeader'
        db.create_table(u'emails_emailheader', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('email', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['emails.EmailMessage'])),
            ('key', self.gf('django.db.models.fields.CharField')(max_length=255, db_index=True)),
            ('value_short', self.gf('django.db.models.fields.CharField')(max_length=255, db_index=True)),
            ('value', self.gf('django.db.models.fields.TextField')()),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, db_index=True, blank=True)),
            ('date_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, db_index=True, blank=True)),
        ))
        db.send_create_signal(u'emails', ['EmailHeader'])

        # Adding unique constraint on 'EmailHeader', fields ['email', 'key']
        db.create_unique(u'emails_emailheader', ['email_id', 'key'])


    def backwards(self, orm):
        # Removing unique constraint on 'EmailHeader', fields ['email', 'key']
        db.delete_unique(u'emails_emailheader', ['email_id', 'key'])

        # Deleting model 'EmailHeader'
        db.delete_table(u'emails_emailheader')


    models = {
        u'emails.emailflag': {
            'Meta': {'unique_together': "(('email', 'flag'),)", 'object_name': 'EmailFlag'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'db_index': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['emails.EmailMessage']"}),
            'flag': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'emails.emailheader': {
            'Meta': {'unique_together': "(('email', 'key'),)", 'object_name': 'EmailHeader'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'db_index': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['emails.EmailMessage']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'}),
            'value': ('django.db.models.fields.TextField', [], {}),
            'value_short': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'})
        },
        u'emails.emailmessage': {
            'Meta': {'object_name': 'EmailMessage'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'db_index': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'raw_body': ('django.db.models.fields.TextField', [], {}),
            'rfc_size': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_index': 'True'}),
            'seq': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'uid': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'db_index': 'True'})
        }
    }

    complete_apps = ['emails']