from rest_framework import serializers
from .models import Quiz


class QuizSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(max_length=65, min_length=4)
    # credit = serializers.IntegerField()
    SubmitionType = serializers.CharField(max_length=200)
    QuizDiscription = serializers.CharField(max_length=200)
    QuizTitle = serializers.CharField(max_length=200)
    attempts = serializers.CharField(max_length=200)
    # id = serializers.CharField(max_length=200, )
    marks = serializers.CharField(max_length=200)
    uplodDocument = serializers.CharField(max_length=200)
    DateOfSubmission = serializers.DateTimeField()
    TotalhrsforAtempting = serializers.CharField(max_length=200)
    class Meta:
        model = Quiz
        fields = ['SubmitionType',
                  'QuizDiscription',
                  'QuizTitle',
                  'attempts',
                  'id',
                  'marks',
                  'uplodDocument',
                  'DateOfSubmission',
                  'TotalhrsforAtempting'
                  ]
