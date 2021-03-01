from django.db import models

# Create your models here.


class Assignment(models.Model):
    # name = models.CharField(max_length=200, unique=True)
    # credit = models.IntegerField(default=None, blank=True, null=True)
    SubmitionType = models.CharField(max_length=200, unique=False)
    assignmentDiscription = models.CharField(max_length=200, unique=False)
    assignmentTitle = models.CharField(max_length=200, unique=False)
    attempts = models.CharField(max_length=200, unique=False)
    # id = models.CharField(max_length=200, unique=True)
    marks = models.CharField(max_length=200, unique=False)
    uplodDocument = models.CharField(max_length=200, unique=False)
    dateOfSubmission = models.DateTimeField(unique=False)
