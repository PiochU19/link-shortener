from django.urls import path

from .views import CreateShortUrl


app_name = 'url_api'


urlpatterns = [
	path('create/', CreateShortUrl.as_view(), name='create-short-url'),
]