# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0004_auto_20150324_1411'),
        ('filer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('caption_text', models.CharField(max_length=255, blank=True, null=True)),
                ('image', filer.fields.image.FilerImageField(to='filer.Image', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, primary_key=True, serialize=False, parent_link=True, to='cms.CMSPlugin')),
                ('name', models.CharField(max_length=50)),
                ('dots', models.BooleanField(default=False)),
                ('fade', models.BooleanField(default=False)),
                ('autoplay', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.AddField(
            model_name='image',
            name='slider',
            field=models.ForeignKey(related_name='images', to='djangocms_simple_slider.Slider'),
            preserve_default=True,
        ),
    ]
