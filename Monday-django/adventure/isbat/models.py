from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=20)
    age=models.IntegerField()

#book author
class Author(models.Model):
    name=models.CharField(max_length=20)
    

class Book(models.Model):
    name=models.CharField(max_length=100)
    publisher=models.ForeignKey(Author,on_delete=models.CASCADE)


#many to many
class Course(models.Model):
    course_name=models.CharField(max_length=100)
    #courses=models.ManyToManyField(Course)


class person(models.Model):
    name=models.CharField(max_length=100)

class registrtaion(models.Model):
    code=models.CharField(max_length=100,unique=True)
    personno=models.OneToOneField(person,primary_key=True,on_delete=models.CASCADE)

class Products(models.Model):
    categories=[('Fruits','Fruits'),
               ('TECH','Technologies'),
               ('electronics','Electric')]
    years=[('2000-2010','legacy'),('2011-2026','NEW')]

    prodname=models.CharField(max_length=100,unique=True)
    productcat=models.CharField(max_length=100,choices=categories)
    prodyear=models.CharField(max_length=100,choices=years)
