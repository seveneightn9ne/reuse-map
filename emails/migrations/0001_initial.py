# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'EmailMessage'
        db.create_table(u'emails_emailmessage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('uid', self.gf('django.db.models.fields.IntegerField')(unique=True, db_index=True)),
            ('raw_body', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'emails', ['EmailMessage'])

        # Adding model 'EmailTag'
        db.create_table(u'emails_emailtag', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('email', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['emails.EmailMessage'])),
            ('tag', self.gf('django.db.models.fields.CharField')(max_length=255, db_index=True)),
        ))
        db.send_create_signal(u'emails', ['EmailTag'])

        # Adding unique constraint on 'EmailTag', fields ['email', 'tag']
        db.create_unique(u'emails_emailtag', ['email_id', 'tag'])


    def backwards(self, orm):
        # Removing unique constraint on 'EmailTag', fields ['email', 'tag']
        db.delete_unique(u'emails_emailtag', ['email_id', 'tag'])

        # Deleting model 'EmailMessage'
        db.delete_table(u'emails_emailmessage')

        # Deleting model 'EmailTag'
        db.delete_table(u'emails_emailtag')


    models = {
        u'emails.emailmessage': {
            'Meta': {'object_name': 'EmailMessage'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'raw_body': ('django.db.models.fields.TextField', [], {}),
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