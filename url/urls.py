from django.urls import path

from .views import redirected


app_name = 'url'


urlpatterns = [
	path('<str:code>/', redirected, name='redirected'),
]