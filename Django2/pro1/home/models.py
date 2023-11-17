from django.db import models

# Create your models here.
class Employee(models.Model):
    emp_id=models.CharField(max_length=50)
    emp_name=models.CharField(max_length=50)
    emp_email=models.EmailField()
    emp_address=models.CharField( max_length=50)