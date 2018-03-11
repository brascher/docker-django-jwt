from django.test import TestCase, Client
from django.urls import reverse

from ..models import Genre
from ..serializers import GenreSerializer

class GenreTest(TestCase):
    """
    Test class for the Genre services
    """

    def setUp(self):
        Genre.objects.create(name="Heavy Metal", description="Metallica belongs here")
        Genre.objects.create(name="Country")
        Genre.objects.create(name="Alt Rock", description="Something different")

        self.response = self.client.get("/api/v1/genre/")

    def test_genre_all_success_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_genre_contains_all(self):
        genres = Genre.objects.all()
        serializer = GenreSerializer(genres, many=True)
        self.assertEqual(self.response.data, serializer.data)
