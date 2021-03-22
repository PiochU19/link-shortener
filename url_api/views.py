from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ShortUrlSerializer
from url.models import ShortUrl
from rest_framework import status


class CreateShortUrl(APIView):

	def post(self, request):

		serializer = ShortUrlSerializer(data=request.data)

		if serializer.is_valid():
			serializer.save()

			return Response(serializer.data, status=status.HTTP_201_CREATED)

		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)