from django.db import models

# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length=200,unique=True)
    credit= models.IntegerField(default=None,blank=True, null=True)

class Module(models.Model):
    # course = models.ForeignKey(Course,on_delete=models.CASCADE)
    name = models.CharField(max_length=10,unique=True)
    description= models.CharField(max_length=600)
    topics= models.CharField(max_length=600)