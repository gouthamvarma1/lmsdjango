from rest_framework import serializers
from django.contrib.auth.models import User
from coursemodules.models import Module

class ModuleSerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        max_length=65, min_length=4)
    description= serializers.EmailField(max_length=255, min_length=4),
    topics= serializers.CharField(max_length=255, min_length=4)
    class Meta:
        model = Module
        fields = ['name','description','topics']


    # def validate(self, attrs):
    #     email = attrs.get('email', '')
    #     if User.objects.filter(email=email).exists():
    #         raise serializers.ValidationError(
    #             {'email': ('Email is already in use')})
    #     return super().validate(attrs)

    # def create(self, validated_data):
    #     return User.objects.create_user(**validated_data)


