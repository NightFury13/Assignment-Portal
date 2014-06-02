# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0002_faculty'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TA',
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
