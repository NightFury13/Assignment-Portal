from django.db import models

# Create your models here.

class Course(models.Model):
    name=models.CharField('Course Name', max_length=100)
    code=models.CharField('Course Code',max_length=15)

class Assignment(models.Model):
    course=models.ForeignKey(Course)
    name=models.CharField('Assignment Name', max_length=50)
    start_time=models.DateTimeField('Start Date')
    end_time=models.DateTimeField('End Date')

class Problem(models.Model):
    assignment=models.ForeignKey(Assignment)
    statement=models.CharField('Problem Statement', max_length=500)
    image=models.ImageField('Problem Image', upload_to='images/problems/%Y/%m/%d', max_length=200)

class User(models.Model):
    name=models.CharField('Name', max_length=100)

#Not sure ->

class Faculty(User):
    pass

class TA(User):
    roll_number=models.CharField('Roll Number', max_length='10')

class Student(User):
    roll_number=models.CharField('Roll Number', max_length='10')

class Fac_Course(models.Model):
    faculty=models.ForeignKey(Faculty)
    course=models.ForeignKey(Course)

class TA_Course(models.Model):
    ta=models.ForeignKey(TA)
    course=models.ForeignKey(Course)

class Student_Course(models.Model):
    student=models.ForeignKey(Student)
    course=models.ForeignKey(Course)

class Submissions(models.Model):
    student=models.ForeignKey(Student)
    problem=models.ForeignKey(Problem)
    image=models.ImageField('Submission Image', upload_to='image/submission/%Y/%m/%d', max_length=200)
    answer=models.CharField('Answer', max_length=1000)
    #expand marks
    #marks=
    #comments=

class TA_Assigned(models.Model):
    ta=models.ForeignKey(TA)
    problem=models.ForeignKey(Problem)
