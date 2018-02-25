from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Genre, Decade
from .serializers import GenreSerializer, DecadeSerializer

class GenreView(APIView):

    permission_classes = (AllowAny,)

    def get(self, request, format=None):
        genre = Genre.objects.all()
        serializer = GenreSerializer(genre, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class DecadeView(APIView):

    permission_classes = (AllowAny,)

    def get(self, request, format=None):
        decade = Decade.objects.all()
        serializer = DecadeSerializer(decade, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)