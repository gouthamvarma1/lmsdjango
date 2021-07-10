from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Module,Course

class ModuleSerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        max_length=65)
    description= serializers.CharField(max_length=255),
    topics= serializers.CharField(max_length=255)
    class Meta:
        model = Module
        fields = ['id','name','description','topics']


class CourseSerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        max_length=65)
    credit= serializers.IntegerField()
    class Meta:
        model = Course
        fields = ['id','name' ,'credit']


    # def validate(self, attrs):
    #     email = attrs.get('email', '')
    #     if User.objects.filter(email=email).exists():
    #         raise serializers.ValidationError(
    #             {'email': ('Email is already in use')})
    #     return super().validate(attrs)

    # def create(self, validated_data):
    #     return User.objects.create_user(**validated_data)


