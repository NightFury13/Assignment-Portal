# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0005_submission'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='submissions',
            field=models.ManyToManyField(to='server.Problem', through='server.Submission'),
            preserve_default=True,
        ),
    ]
