# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-11-27 06:49
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import pyuploadcare.dj.models
import tinymce.models
import url_or_relative_url_field.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.TextField(max_length=400)),
                ('pro_id', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('bio', tinymce.models.HTMLField()),
                ('profile_photo', pyuploadcare.dj.models.ImageField(blank=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('phone_number', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('design', models.IntegerField(default=0)),
                ('usability', models.IntegerField(default=0)),
                ('content', models.IntegerField(default=0)),
                ('image_landing', models.ImageField(upload_to='landing/')),
                ('description', tinymce.models.HTMLField(blank=True, max_length=200)),
                ('link', url_or_relative_url_field.fields.URLOrRelativeURLField()),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Rates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('design', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(10)])),
                ('usability', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(10)])),
                ('content', models.IntegerField(default=0, validators=[10])),
                ('project', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.AddField(
            model_name='comments',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='rates',
            unique_together=set([('user', 'design', 'usability', 'content', 'project')]),
        ),
        migrations.AlterIndexTogether(
            name='rates',
            index_together=set([('user', 'design', 'usability', 'content', 'project')]),
        ),
    ]
