from django.db import models

class Department(models.Model):
    dept_name=models.CharField(max_length=100)
    dept_desc=models.CharField(max_length=100)

class Doctor(models.Model):
    name=models.CharField(max_length=100)
    username=models.CharField(max_length=100,null=True,blank=True)
    password=models.CharField(max_length=100,null=True,blank=True)
    image=models.ImageField(upload_to='photos/doctors',blank=True)
    mobile=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    department=models.ForeignKey(Department,on_delete=models.CASCADE)

class Patient(models.Model):
    name=models.CharField(max_length=100)
    username=models.CharField(max_length=100,null=True,blank=True)
    password=models.CharField(max_length=100,null=True,blank=True)
    image=models.ImageField(upload_to='photos/doctors',blank=True)
    symptoms=models.CharField(max_length=100,null=True,blank=True)
    mobile=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    dob=models.DateField()
    gender=models.CharField(max_length=100)