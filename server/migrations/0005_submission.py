# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0004_problem_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('student', models.ForeignKey(to='server.Student', to_field='id')),
                ('problem', models.ForeignKey(to='server.Problem', to_field='id')),
                ('image', models.ImageField(upload_to=b'image/submission/%Y/%m/%d', max_length=200, verbose_name=b'Submission Image')),
                ('answer', models.CharField(max_length=1000, verbose_name=b'Answer')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
