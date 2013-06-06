# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'EmailMessage.date_created'
        db.add_column(u'emails_emailmessage', 'date_created',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2013, 6, 5, 0, 0), db_index=True, blank=True),
                      keep_default=False)

        # Adding field 'EmailMessage.date_modified'
        db.add_column(u'emails_emailmessage', 'date_modified',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2013, 6, 5, 0, 0), db_index=True, blank=True),
                      keep_default=False)

        # Adding field 'EmailFlag.date_created'
        db.add_column(u'emails_emailflag', 'date_created',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2013, 6, 5, 0, 0), db_index=True, blank=True),
                      keep_default=False)

        # Adding field 'EmailFlag.date_modified'
        db.add_column(u'emails_emailflag', 'date_modified',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2013, 6, 5, 0, 0), db_index=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'EmailMessage.date_created'
        db.delete_column(u'emails_emailmessage', 'date_created')

        # Deleting field 'EmailMessage.date_modified'
        db.delete_column(u'emails_emailmessage', 'date_modified')

        # Deleting field 'EmailFlag.date_created'
        db.delete_column(u'emails_emailflag', 'date_created')

        # Deleting field 'EmailFlag.date_modified'
        db.delete_column(u'emails_emailflag', 'date_modified')


    models = {
        u'emails.emailflag': {
            'Meta': {'unique_together': "(('email', 'flag'),)", 'object_name': 'EmailFlag'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'db_index': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['emails.EmailMessage']"}),
            'flag': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
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