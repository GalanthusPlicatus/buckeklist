from base.models import Dream, Budget, BudgetType
from django.test import TestCase, RequestFactory, Client
from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from base.models import Dream

# Code without tests is broken as designed.


class FirstTestForViewTests(APITestCase):

    def setUp(self):
        self.client = APIClient()

    def test_create_dream(self):
        url = reverse('api:dream_list')
        payload = {
            'name': 'buy bucket',
            'description': 'chilling out',
            'status': Dream.CREATED,
            'visibility': Dream.PUBLIC,
            }
        # print data
        response = self.client.post(url, payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # self.assertEqual(Dream.objects.count(), 1)
        # self.assertEqual(Dream.objects.get().name, 'buy bucket')
