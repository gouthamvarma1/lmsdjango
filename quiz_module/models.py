from django.db import models

# Create your models here.


class Quiz(models.Model):
    # name = models.CharField(max_length=200, unique=True)
    # credit = models.IntegerField(default=None, blank=True, null=True)
    SubmitionType = models.CharField(max_length=200, unique=False)
    QuizDiscription = models.CharField(max_length=200, unique=False)
    QuizTitle = models.CharField(max_length=200, unique=False)
    attempts = models.CharField(max_length=200, unique=False)
    # id = models.CharField(max_length=200, unique=True)
    marks = models.CharField(max_length=200, unique=False)
    uplodDocument = models.CharField(max_length=200, unique=False)
    DateOfSubmission = models.DateTimeField(unique=False)
    TotalhrsforAtempting = models.CharField(max_length=200, unique=False)

