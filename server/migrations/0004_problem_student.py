# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('server', '0003_ta'),
    ]

    operations = [
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('assignment', models.ForeignKey(to='server.Assignment', to_field='id')),
                ('statement', models.CharField(max_length=500, verbose_name=b'Problem Statement')),
                ('image', models.ImageField(upload_to=b'images/problems/%Y/%m/%d', max_length=200, verbose_name=b'Problem Image')),
                ('tas', models.ManyToManyField(to='server.TA')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL, to_field='id')),
                ('roll_number', models.CharField(max_length=b'10', verbose_name=b'Roll Number')),
                ('courses', models.ManyToManyField(to='server.Course')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
