# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Domain'
        db.create_table('emails_domain', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('last_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=256)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='email_domain_set', to=orm['auth.User'])),
        ))
        db.send_create_signal('emails', ['Domain'])

        # Deleting field 'EmailRedirect.pub_date'
        db.delete_column('emails_redirect', 'pub_date')

        # Adding field 'EmailRedirect.last_modified'
        db.add_column('emails_redirect', 'last_modified',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2012, 12, 31, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'EmailRedirect.new_domain'
        db.add_column('emails_redirect', 'new_domain',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['emails.Domain'], null=True),
                      keep_default=False)

        # Deleting field 'Email.homedir'
        db.delete_column('emails_email', 'homedir')

        # Deleting field 'Email.gid'
        db.delete_column('emails_email', 'gid')

        # Deleting field 'Email.pub_date'
        db.delete_column('emails_email', 'pub_date')

        # Deleting field 'Email.remove'
        db.delete_column('emails_email', 'remove')

        # Deleting field 'Email.uid'
        db.delete_column('emails_email', 'uid')

        # Adding field 'Email.last_modified'
        db.add_column('emails_email', 'last_modified',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2012, 12, 31, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'Email.new_domain'
        db.add_column('emails_email', 'new_domain',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['emails.Domain'], null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Domain'
        db.delete_table('emails_domain')


        # User chose to not deal with backwards NULL issues for 'EmailRedirect.pub_date'
        raise RuntimeError("Cannot reverse this migration. 'EmailRedirect.pub_date' and its values cannot be restored.")
        # Deleting field 'EmailRedirect.last_modified'
        db.delete_column('emails_redirect', 'last_modified')

        # Deleting field 'EmailRedirect.new_domain'
        db.delete_column('emails_redirect', 'new_domain_id')

        # Adding field 'Email.homedir'
        db.add_column('emails_email', 'homedir',
                      self.gf('django.db.models.fields.CharField')(default='/var/mail', max_length=100),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Email.gid'
        raise RuntimeError("Cannot reverse this migration. 'Email.gid' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Email.pub_date'
        raise RuntimeError("Cannot reverse this migration. 'Email.pub_date' and its values cannot be restored.")
        # Adding field 'Email.remove'
        db.add_column('emails_email', 'remove',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Email.uid'
        raise RuntimeError("Cannot reverse this migration. 'Email.uid' and its values cannot be restored.")
        # Deleting field 'Email.last_modified'
        db.delete_column('emails_email', 'last_modified')

        # Deleting field 'Email.new_domain'
        db.delete_column('emails_email', 'new_domain_id')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'domains.domain': {
            'Meta': {'unique_together': "(('name', 'parent'),)", 'object_name': 'Domain'},
            'dns': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'enable': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ipv4': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ipv6': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'mail': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'subdomains'", 'null': 'True', 'to': "orm['domains.Domain']"}),
            'pub_date': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'serial': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'emails.domain': {
            'Meta': {'object_name': 'Domain'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '256'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'email_domain_set'", 'to': "orm['auth.User']"})
        },
        'emails.email': {
            'Meta': {'object_name': 'Email'},
            'domain': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['domains.Domain']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'login': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'new_domain': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['emails.Domain']", 'null': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'emails.emailredirect': {
            'Meta': {'unique_together': "(('alias', 'domain', 'email'),)", 'object_name': 'EmailRedirect', 'db_table': "'emails_redirect'"},
            'alias': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'domain': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['domains.Domain']"}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'new_domain': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['emails.Domain']", 'null': 'True'})
        },
        'emails.message': {
            'Meta': {'object_name': 'Message'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lang': ('django.db.models.fields.CharField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'purpose': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['emails']