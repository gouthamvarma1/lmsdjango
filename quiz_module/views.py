from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from .serializers import QuizSerializer
from rest_framework.response import Response
from rest_framework import status ,viewsets
from django.conf import settings
from django.contrib import auth
from .models import Quiz
# Create your views here.

    
class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all().order_by('id')
    serializer_class = QuizSerializer