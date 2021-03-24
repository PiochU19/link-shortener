from django.db import models


# Imports to generate unique code

import string
import random


# Function returning code

def code_generator():

	possible_chars = '0123456789' + string.ascii_lowercase + string.ascii_uppercase
	code = ''.join(random.choice(possible_chars) for i in range(5))

	return code


# Function to add 'http://' to URL

def url_validation(url):

	if not '://' in url:
		url = 'http://' + url

	return url


class ShortUrl(models.Model):
	short_url 		= models.CharField(max_length=5, blank=True)
	url 			= models.URLField(max_length=255)
	clicks			= models.IntegerField(default=0)

	def save(self, *args, **kwargs):

		if not self.id:
			self.url = url_validation(self.url)

			self.short_url = code_generator()

			x = ShortUrl.objects.filter(short_url=self.short_url).count()

			while x > 0:

				self.short_url = code_generator()

				x = ShortUrl.objects.filter(short_url=self.short_url).count()

		return super().save(*args, **kwargs)

	def click(self):

		self.clicks += 1
		self.save()

	def __str__(self):

		return f"{self.url}"