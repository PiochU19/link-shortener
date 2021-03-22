from django.contrib import admin
from .models import ShortUrl


# Custom ShortUrl adming page

class ShortUrlAdmin(admin.ModelAdmin):

	list_display = ('url', 'clicks')


admin.site.register(ShortUrl, ShortUrlAdmin)