from rest_framework import serializers
from url.models import ShortUrl


class ShortUrlSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = ShortUrl
		fields = ('url', 'short_url')