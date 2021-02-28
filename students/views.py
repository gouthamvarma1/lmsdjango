from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status ,viewsets
from django.conf import settings
from django.contrib import auth
from .models import Students
# Create your views here.


class ModuleView(GenericAPIView):
    serializer_class = StudentSerializer

    def post(self, request):
        serializer = StudentSerializer(data=request.data,context={'request': request})
        print(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Students.objects.all().order_by('id')
    serializer_class = StudentSerializer
