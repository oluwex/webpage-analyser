from rest_framework import status
from rest_framework.test import APITestCase

from django.shortcuts import reverse

class AccountsAPITest(APITestCase):
    password = 'Abcabc123'

    @classmethod
    def setUpTestData(cls):
        cls.content = open("C:/Users/Habeeb/Documents/Docs/django-docs-2.1-en/ref/templates/builtins.html", 'r',
                       encoding='utf8')

    def test_invalid_url(self):
        data = {'url': 'docs.djangoproject.com/en/2.2/ref/templates/builtins/'}
        url = reverse('analyser-api:index-api')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_analysis_successful(self):
        data = {'url': 'https://docs.djangoproject.com/en/2.2/ref/templates/builtins/'}
        url = reverse('analyser-api:index-api')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('number_of_tables'), 9)
        self.assertGreater(len(response.data.get('result_summary')), 0)