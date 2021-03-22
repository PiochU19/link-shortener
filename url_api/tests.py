from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from url.models import ShortUrl


class TestApi(APITestCase):

	def test_create(self):

		data = {"url": "www.google.com"}

		url = reverse('url_api:create-short-url')

		response = self.client.post(url, data)

		self.assertEqual(response.status_code, status.HTTP_201_CREATED)

		obj = ShortUrl.objects.get(id=1)

		self.assertEqual(str(obj), 'http://www.google.com')

	def test_create_fail(self):

		url = reverse('url_api:create-short-url')

		response = self.client.post(url)

		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)