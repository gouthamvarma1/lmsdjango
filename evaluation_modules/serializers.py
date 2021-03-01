from rest_framework import serializers
from .models import Assignment


class AssignmentSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(max_length=65, min_length=4)
    # credit = serializers.IntegerField()
    SubmitionType = serializers.CharField(max_length=200)
    assignmentDiscription = serializers.CharField(max_length=200)
    assignmentTitle = serializers.CharField(max_length=200)
    attempts = serializers.CharField(max_length=200)
    # id = serializers.CharField(max_length=200, )
    marks = serializers.CharField(max_length=200)
    uplodDocument = serializers.CharField(max_length=200)
    dateOfSubmission = serializers.DateTimeField()

    class Meta:
        model = Assignment
        fields = ['SubmitionType',
                  'assignmentDiscription',
                  'assignmentTitle',
                  'attempts',
                  'id',
                  'marks',
                  'uplodDocument',
                  'dateOfSubmission'
                  ]
