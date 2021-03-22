from django.test import TestCase
from .models import ShortUrl
from django.urls import reverse


class TestShortUrl(TestCase):

	@classmethod
	def setUpTestData(cls):

		url = ShortUrl(url='www.google.com')
		url.save()

	def test_long_url(self):

		url = ShortUrl.objects.get(id=1)

		self.assertEqual(url.url, 'http://www.google.com')
		self.assertEqual(str(url), url.url)

	def test_short_url(self):

		url = ShortUrl.objects.get(id=1)
		short = url.short_url

		self.assertEqual(len(url.short_url), 5)

		_url = ShortUrl.objects.get(short_url=short)

		self.assertEqual(_url.url, 'http://www.google.com')

	def test_click(self):

		url = ShortUrl.objects.get(id=1)

		self.assertEqual(url.clicks, 0)

		url.click()

		self.assertEqual(url.clicks, 1)

	def test_redirect(self):

		obj = ShortUrl.objects.get(id=1)

		url = reverse('url:redirected-page', kwargs={'code': f"{obj.short_url}"})
		response = self.client.get(url)

		self.assertRedirects(response, f"{obj.url}", fetch_redirect_response=False)