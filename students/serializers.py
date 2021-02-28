from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Students


class StudentSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=65, min_length=4)
    email = serializers.CharField(max_length=65, min_length=10)
    gender = serializers.CharField(max_length=8, min_length=4)
    id= serializers.IntegerField()
    class Meta:
        model = Students
        fields = ['id' ,'name','email','gender']


