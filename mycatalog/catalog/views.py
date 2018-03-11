from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Genre, Decade
from .renderers import DecadeRenderer, GenreRenderer
from .serializers import GenreSerializer, DecadeSerializer

# /genre service; GET and POST
class GenreListView(APIView):

    permission_classes = (AllowAny,)
    renderer_classes = (GenreRenderer,)
    serializer_class = GenreSerializer

    def get(self, request, format=None):
        genre = Genre.objects.all()
        serializer = self.serializer_class(genre, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data.get("genre", {}), partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

# /genre/:id service; GET and PUT
class GenreDetailView(APIView):

    permission_classes = (AllowAny,)
    renderer_classes = (GenreRenderer,)
    serializer_class = GenreSerializer

    def get(self, request, pk, format=None):
        genre = Genre.objects.get(pk=pk)
        serializer = self.serializer_class(genre)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        genre = Genre.objects.get(pk=pk)
        serializer = self.serializer_class(genre, data=request.data.get("genre", {}), partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

# /decade service; GET only
class DecadeListView(APIView):

    permission_classes = (AllowAny,)
    renderer_classes = (DecadeRenderer,)
    serializer_class = DecadeSerializer

    def get(self, request, format=None):
        decade = Decade.objects.all()
        serializer = self.serializer_class(decade, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# /decade/:id service; GET only
class DecadeDetailView(APIView):
    
    permission_classes = (AllowAny,)
    renderer_classes = (DecadeRenderer,)
    serializer_class = DecadeSerializer

    def get(self, request, pk, format=None):
        decade = Decade.objects.get(pk=pk)
        serializer = self.serializer_class(decade)
        return Response(serializer.data, status=status.HTTP_200_OK)

class MissingView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, format=None):
        return Response(status=status.HTTP_404_NOT_FOUND)