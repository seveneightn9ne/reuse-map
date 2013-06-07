# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'EmailMessage', fields ['uid']
        db.delete_unique(u'emails_emailmessage', ['uid'])

        # Adding field 'EmailMessage.username'
        db.add_column(u'emails_emailmessage', 'username',
                      self.gf('django.db.models.fields.CharField')(default='unknown', max_length=255, db_index=True),
                      keep_default=False)

        # Adding field 'EmailMessage.host'
        db.add_column(u'emails_emailmessage', 'host',
                      self.gf('django.db.models.fields.CharField')(default='unknown', max_length=255, db_index=True),
                      keep_default=False)

        # Adding unique constraint on 'EmailMessage', fields ['username', 'host', 'uid']
        db.create_unique(u'emails_emailmessage', ['username', 'host', 'uid'])


    def backwards(self, orm):
        # Removing unique constraint on 'EmailMessage', fields ['username', 'host', 'uid']
        db.delete_unique(u'emails_emailmessage', ['username', 'host', 'uid'])

        # Deleting field 'EmailMessage.username'
        db.delete_column(u'emails_emailmessage', 'username')

        # Deleting field 'EmailMessage.host'
        db.delete_column(u'emails_emailmessage', 'host')

        # Adding unique constraint on 'EmailMessage', fields ['uid']
        db.create_unique(u'emails_emailmessage', ['uid'])


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
            'Meta': {'unique_together': "(('uid', 'username', 'host'),)", 'object_name': 'EmailMessage'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'db_index': 'True', 'blank': 'True'}),
            'host': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'raw_body': ('django.db.models.fields.TextField', [], {}),
            'rfc_size': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_index': 'True'}),
            'seq': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'uid': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'})
        }
    }

    complete_apps = ['emails']