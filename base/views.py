# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import authentication, permissions

from django.shortcuts import render
from rest_framework import generics

from models import Dream
from serializer import DreamSerializer, BudgetSerializer, BudgetTypeSerializer
# Create your views here.


class BucketListApi(generics.ListCreateAPIView):
    """To list all dreams"""
    queryset = Dream.objects.all()
    serializer_class = DreamSerializer

# class BucketApi(generics.ListCreateAPIView):
#     """To list all dreams"""
#     queryset = Dream.objects.all()
#     serializer_class = DreamSerializer    

