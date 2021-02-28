from django.db import models

# Create your models here.


class Students(models.Model):
    # course = models.ForeignKey(Course,on_delete=models.CASCADE)
    id =models.CharField(max_length=50,primary_key=True)
    name = models.CharField(max_length=50)
    email= models.CharField(max_length=600)
    gender= models.CharField(max_length=6)