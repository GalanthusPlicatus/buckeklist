from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
# from rest_framework import authentication, permissions

from django.shortcuts import render
from rest_framework import generics

from models import Dream
from serializer import DreamSerializer, BudgetSerializer, BudgetTypeSerializer
# Create your views here.



class DreamListApi(generics.ListCreateAPIView):
    """To list all dreams"""
    queryset = Dream.objects.all()
    serializer_class = DreamSerializer


class DreamDetailsApi(APIView):
    def get_object(self, pk):
        try:
            return Dream.objects.get(pk=pk)
        except Dream.DoesNotExist:
            raise Http404
    # raise Exception("Fix me")

    def get(self, request, pk, format=None):
        dream = self.get_object(pk)
        serializer = DreamSerializer(dream)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        dream = self.get_object(pk)
        serializer = DreamSerializer(dream, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        dream = self.get_object(pk)
        dream.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
