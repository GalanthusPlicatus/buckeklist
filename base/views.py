from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import authentication, permissions

from django.shortcuts import render
from rest_framework import generics

from models import Dream
from serializer import DreamSerializer
# Create your views here.


class BucketListApi(generics.ListCreateAPIView):
    """To list all dreams"""
    queryset = Dream.objects.all()
    serializer_class = DreamSerializer


class BucketListDetailApi(APIView):
    """Get dream details for specified dream_id"""

    def get(self, request):
        dream_id = request.GET.get('pk')
        dream_id
        raise Exception("fix")
        try:
            dream = Dream.objects.get(pk=dream_id)
            serializer_class = DreamSerializer
            return Response(serializer.data)
        except:
            raise Http404
