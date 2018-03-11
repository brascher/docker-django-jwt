from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Genre, Decade
from .renderers import DecadeRenderer, GenreRenderer
from .serializers import GenreSerializer, DecadeSerializer

# /genre service; GET only
class GenreView(APIView):

    permission_classes = (AllowAny,)
    renderer_classes = (GenreRenderer,)

    def get(self, request, format=None):
        genre = Genre.objects.all()
        serializer = GenreSerializer(genre, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# /decade service; GET only
class DecadeView(APIView):

    permission_classes = (AllowAny,)
    renderer_classes = (DecadeRenderer,)

    def get(self, request, format=None):
        decade = Decade.objects.all()
        serializer = DecadeSerializer(decade, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class MissingView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, format=None):
        return Response(status=status.HTTP_404_NOT_FOUND)