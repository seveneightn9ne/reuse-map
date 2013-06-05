# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'EmailTag', fields ['email', 'tag']
        db.delete_unique(u'emails_emailtag', ['email_id', 'tag'])

        # Deleting model 'EmailTag'
        db.delete_table(u'emails_emailtag')

        # Adding model 'EmailFlag'
        db.create_table(u'emails_emailflag', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('email', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['emails.EmailMessage'])),
            ('flag', self.gf('django.db.models.fields.CharField')(max_length=255, db_index=True)),
        ))
        db.send_create_signal(u'emails', ['EmailFlag'])

        # Adding unique constraint on 'EmailFlag', fields ['email', 'flag']
        db.create_unique(u'emails_emailflag', ['email_id', 'flag'])


    def backwards(self, orm):
        # Removing unique constraint on 'EmailFlag', fields ['email', 'flag']
        db.delete_unique(u'emails_emailflag', ['email_id', 'flag'])

        # Adding model 'EmailTag'
        db.create_table(u'emails_emailtag', (
            ('tag', self.gf('django.db.models.fields.CharField')(max_length=255, db_index=True)),
            ('email', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['emails.EmailMessage'])),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'emails', ['EmailTag'])

        # Adding unique constraint on 'EmailTag', fields ['email', 'tag']
        db.create_unique(u'emails_emailtag', ['email_id', 'tag'])

        # Deleting model 'EmailFlag'
        db.delete_table(u'emails_emailflag')


    models = {
        u'emails.emailflag': {
            'Meta': {'unique_together': "(('email', 'flag'),)", 'object_name': 'EmailFlag'},
            'email': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['emails.EmailMessage']"}),
            'flag': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'emails.emailmessage': {
            'Meta': {'object_name': 'EmailMessage'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'raw_body': ('django.db.models.fields.TextField', [], {}),
            'rfc_size': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_index': 'True'}),
            'seq': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'uid': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'db_index': 'True'})
        }
    }

    complete_apps = ['emails']