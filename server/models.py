from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Course(models.Model):
    def __unicode__(self):
        return self.name
    name=models.CharField('Course Name', max_length=100)
    code=models.CharField('Course Code',max_length=15)

class Assignment(models.Model):
    course=models.ForeignKey(Course)
    name=models.CharField('Assignment Name', max_length=50)
    start_time=models.DateTimeField('Start Date')
    end_time=models.DateTimeField('End Date')


class Person(models.Model):
    user = models.OneToOneField(User)
    courses=models.ManyToManyField(Course) 
    class Meta:
        abstract = True

class Faculty(Person):
    pass

class TA(Person):
    roll_number=models.CharField('Roll Number', max_length='10')

class Problem(models.Model):
    assignment=models.ForeignKey(Assignment)
    statement=models.CharField('Problem Statement', max_length=500)
    image=models.ImageField('Problem Image', upload_to='images/problems/%Y/%m/%d', max_length=200)
    tas=models.ManyToManyField(TA)

class Student(Person):
    roll_number=models.CharField('Roll Number', max_length='10')
    submissions=models.ManyToManyField(Problem, through='Submission')

class Submission(models.Model):
    student=models.ForeignKey(Student)
    problem=models.ForeignKey(Problem)
    image=models.ImageField('Submission Image', upload_to='image/submission/%Y/%m/%d', max_length=200)
    answer=models.CharField('Answer', max_length=1000)
    #expand marks
    #marks=
    #comments=
    #checked by TA (if multiple ta's assigned one problem)
