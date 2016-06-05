from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework import viewsets
from rest_framework import generics


from base.serializers import UserSerializer
from models import Dream
from serializer import(
    DreamSerializer, BudgetSerializer, BudgetTypeSerializer,
    UserSerializer
)

from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.shortcuts import render

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


class UserViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    def list(self, request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)
