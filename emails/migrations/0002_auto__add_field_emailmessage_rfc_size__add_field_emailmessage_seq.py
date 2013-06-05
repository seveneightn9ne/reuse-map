# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'EmailMessage.rfc_size'
        db.add_column(u'emails_emailmessage', 'rfc_size',
                      self.gf('django.db.models.fields.IntegerField')(null=True, db_index=True),
                      keep_default=False)

        # Adding field 'EmailMessage.seq'
        db.add_column(u'emails_emailmessage', 'seq',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'EmailMessage.rfc_size'
        db.delete_column(u'emails_emailmessage', 'rfc_size')

        # Deleting field 'EmailMessage.seq'
        db.delete_column(u'emails_emailmessage', 'seq')


    models = {
        u'emails.emailmessage': {
            'Meta': {'object_name': 'EmailMessage'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'raw_body': ('django.db.models.fields.TextField', [], {}),
            'rfc_size': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_index': 'True'}),
            'seq': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'uid': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'db_index': 'True'})
        },
        u'emails.emailtag': {
            'Meta': {'unique_together': "(('email', 'tag'),)", 'object_name': 'EmailTag'},
            'email': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['emails.EmailMessage']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tag': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'})
        }
    }

    complete_apps = ['emails']