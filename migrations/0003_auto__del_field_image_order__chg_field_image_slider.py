# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Image.order'
        db.delete_column('djangocms_simple_slider_image', 'order')


        # Changing field 'Image.slider'
        db.alter_column('djangocms_simple_slider_image', 'slider_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['djangocms_simple_slider.Slider']))

    def backwards(self, orm):
        # Adding field 'Image.order'
        db.add_column('djangocms_simple_slider_image', 'order',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=1, db_index=True),
                      keep_default=False)


        # Changing field 'Image.slider'
        db.alter_column('djangocms_simple_slider_image', 'slider_id', self.gf('adminsortable.fields.SortableForeignKey')(to=orm['djangocms_simple_slider.Slider']))

    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80', 'unique': 'True'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'blank': 'True', 'to': "orm['auth.Permission']"})
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
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'symmetrical': 'False', 'related_name': "'user_set'", 'to': "orm['auth.Group']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'symmetrical': 'False', 'related_name': "'user_set'", 'to': "orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '30', 'unique': 'True'})
        },
        'cms.cmsplugin': {
            'Meta': {'object_name': 'CMSPlugin'},
            'changed_date': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now': 'True'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.CMSPlugin']", 'blank': 'True', 'null': 'True'}),
            'placeholder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'}),
            'plugin_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'blank': 'True', 'null': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'cms.placeholder': {
            'Meta': {'object_name': 'Placeholder'},
            'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'db_table': "'django_content_type'", 'object_name': 'ContentType'},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'djangocms_simple_slider.image': {
            'Meta': {'object_name': 'Image'},
            'caption_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['filer.Image']", 'null': 'True'}),
            'slider': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['djangocms_simple_slider.Slider']", 'related_name': "'images'"})
        },
        'djangocms_simple_slider.slider': {
            'Meta': {'_ormbases': ['cms.CMSPlugin'], 'object_name': 'Slider'},
            'autoplay': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'primary_key': 'True', 'unique': 'True', 'to': "orm['cms.CMSPlugin']"}),
            'dots': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'fade': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'filer.file': {
            'Meta': {'object_name': 'File'},
            '_file_size': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '255', 'blank': 'True', 'null': 'True'}),
            'folder': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'to': "orm['filer.Folder']", 'related_name': "'all_files'", 'null': 'True'}),
            'has_all_mandatory_data': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_public': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'blank': 'True'}),
            'original_filename': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True', 'null': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'to': "orm['auth.User']", 'related_name': "'owned_files'", 'null': 'True'}),
            'polymorphic_ctype': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']", 'related_name': "'polymorphic_filer.file_set'", 'null': 'True'}),
            'sha1': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '40', 'blank': 'True'}),
            'uploaded_at': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now_add': 'True'})
        },
        'filer.folder': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('parent', 'name'),)", 'object_name': 'Folder'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now_add': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'to': "orm['auth.User']", 'related_name': "'filer_owned_folders'", 'null': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'to': "orm['filer.Folder']", 'related_name': "'children'", 'null': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'uploaded_at': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now_add': 'True'})
        },
        'filer.image': {
            'Meta': {'object_name': 'Image'},
            '_height': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            '_width': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'author': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True', 'null': 'True'}),
            'date_taken': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'null': 'True'}),
            'default_alt_text': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True', 'null': 'True'}),
            'default_caption': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True', 'null': 'True'}),
            'file_ptr': ('django.db.models.fields.related.OneToOneField', [], {'primary_key': 'True', 'unique': 'True', 'to': "orm['filer.File']"}),
            'must_always_publish_author_credit': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'must_always_publish_copyright': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'subject_location': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '64', 'blank': 'True', 'null': 'True'})
        }
    }

    complete_apps = ['djangocms_simple_slider']