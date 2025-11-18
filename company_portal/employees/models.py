from django.db import models

# Create your models here.


class Employee(models.Model):
    emp_id=models.IntegerField()
    emp_name=models.CharField(max_length=20)
    age=models.IntegerField()
    salary=models.IntegerField()
    designation=models.CharField(max_length=20)
    email=models.CharField(max_length=20)