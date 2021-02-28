from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from .serializers import AssignmentSerializer
from rest_framework.response import Response
from rest_framework import status ,viewsets
from django.conf import settings
from django.contrib import auth
from .models import Assignment
# Create your views here.

    
class AssignmentViewSet(viewsets.ModelViewSet):
    queryset = Assignment.objects.all().order_by('id')
    serializer_class = AssignmentSerializer