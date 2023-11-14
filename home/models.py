from django.db import models

# Create your models here.
class student(models.Model):
    name=models.CharField(max_length=20)
    age=models.IntegerField()
class Employee(models.Model):
    empid=models.IntegerField()
    name=models.CharField(max_length=30)
    age=models.IntegerField()
    place=models.CharField(max_length=30)
    salary=models.IntegerField()
    designation=models.CharField(max_length=30)
