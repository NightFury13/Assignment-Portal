# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'Course Name')),
                ('code', models.CharField(max_length=15, verbose_name=b'Course Code')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('course', models.ForeignKey(to='server.Course', to_field='id')),
                ('name', models.CharField(max_length=50, verbose_name=b'Assignment Name')),
                ('start_time', models.DateTimeField(verbose_name=b'Start Date')),
                ('end_time', models.DateTimeField(verbose_name=b'End Date')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
