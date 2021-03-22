from django.shortcuts import redirect, get_object_or_404
from .models import ShortUrl


def redirected(request, code):

	db_url = get_object_or_404(ShortUrl, short_url=code)
	db_url.click()

	return redirect(db_url.url)