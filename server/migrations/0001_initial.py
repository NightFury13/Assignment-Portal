# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='Course Name')),
                ('code', models.CharField(max_length=15, verbose_name='Course Code')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Assignment',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('course', models.ForeignKey(to='server.Course', to_field=u'id')),
                ('name', models.CharField(max_length=50, verbose_name='Assignment Name')),
                ('start_time', models.DateTimeField(verbose_name='Start Date')),
                ('end_time', models.DateTimeField(verbose_name='End Date')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('courses', models.ManyToManyField(to='server.Course')),
            ],
            options={
                u'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TA',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('roll_number', models.CharField(max_length='10', verbose_name='Roll Number')),
                ('courses', models.ManyToManyField(to='server.Course')),
            ],
            options={
                u'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Problem',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('assignment', models.ForeignKey(to='server.Assignment', to_field=u'id')),
                ('statement', models.CharField(max_length=500, verbose_name='Problem Statement')),
                ('image', models.ImageField(upload_to='images/problems/%Y/%m/%d', verbose_name='Problem Image')),
                ('tas', models.ManyToManyField(to='server.TA')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('roll_number', models.CharField(max_length='10', verbose_name='Roll Number')),
                ('courses', models.ManyToManyField(to='server.Course')),
                ('submissions', models.ManyToManyField(to='server.Problem')),
            ],
            options={
                u'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('student', models.ForeignKey(to='server.Student', to_field=u'id')),
                ('problem', models.ForeignKey(to='server.Problem', to_field=u'id')),
                ('image', models.ImageField(upload_to='image/submission/%Y/%m/%d', verbose_name='Submission Image')),
                ('answer', models.CharField(max_length=1000, verbose_name='Answer')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
