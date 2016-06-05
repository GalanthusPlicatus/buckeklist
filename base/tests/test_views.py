from base.models import Dream, Budget, BudgetType
from django.test import TestCase, RequestFactory, Client
from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from base.serializer import *

# Code without tests is broken as designed.


class FirstTestForView(APITestCase):

    def test_create_dream(self):
        url = reverse('api-dream')
        data = {'name': 'buy bucket'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Dream.objects.count(), 1)
        self.assertEqual(Dream.objects.get().name, 'buy bucket')
