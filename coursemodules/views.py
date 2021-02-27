import jwt
from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from .serializers import ModuleSerializer
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from django.contrib import auth
# Create your views here.


class ModuleView(GenericAPIView):
    serializer_class = ModuleSerializer

    def post(self, request):
        serializer = ModuleSerializer(data=request.data,context={'request': request})
        print(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
