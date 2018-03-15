from django.test import RequestFactory, TestCase, Client
from django.urls import resolve

from ..models import Genre
from ..serializers import GenreSerializer
from ..views import GenreDetailView, GenreListView

class GenreTest(TestCase):
    """
    Test class for the Genre model, serializer, and views
    """

    def setUp(self):
        self.request_factory = RequestFactory()
        self.name = "Heavy Metal"
        self.description = "Metallica belongs here"

    def create_genre(self):
        return Genre.objects.create(name=self.name, description=self.description)

    def test_genre_create(self):
        """
        Simple model test
        """
        new_genre = self.create_genre()
        self.assertTrue(isinstance(new_genre, Genre))
        self.assertEqual(new_genre.name, self.name)
        self.assertEqual(new_genre.description, self.description)

    def test_genre_list_success_status_code(self):
        """
        Genres list status code is correct
        """
        request = self.request_factory.get("/api/v1/genre/")
        response = GenreListView.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_genre_detail_success_status_code(self):
        """
        Genre detail status code is correct
        """
        request = self.request_factory.get("/api/v1/genre/1/")
        response = GenreDetailView.as_view()(request, pk=1)
        self.assertEqual(response.status_code, 200)

    def test_genre_not_found_status(self):
        """
        Genre not found status code is correct
        """
        request = self.request_factory.get("/api/v1/genre/99/")
        response = GenreDetailView.as_view()(request, pk=99)
        self.assertEquals(response.status_code, 404)

    def test_genre_url_resolves_genre_list_view(self):
        """
        Genres list url calls the correct view
        """
        view = resolve("/api/v1/genre/")
        self.assertEquals(view.view_name, "genres")

    def test_genre_with_id_url_resolves_genre_detail_view(self):
        """
        Genre detail url calls the correct view
        """
        view = resolve("/api/v1/genre/1/")
        self.assertEquals(view.view_name, "genre")

    def test_genre_serializer_fields(self):
        """
        Genre serializer returns the correct fields
        """
        expected_fields = ["id", "name", "description", "updated_at"]
        test_genre = Genre.objects.get(pk=1)
        serializer = GenreSerializer(test_genre)
        self.assertCountEqual(serializer.data.keys(), expected_fields)

    def test_genre_serializer_content(self):
        """
        Genre serializer returns the correct data
        """
        genre_pk = 1
        genre_name = "Classical"
        genre_description = ""
        test_genre = Genre.objects.get(pk=genre_pk)
        serializer = GenreSerializer(test_genre)
        self.assertEqual(serializer.data["id"], genre_pk)
        self.assertEqual(serializer.data["name"], genre_name)
        self.assertEqual(serializer.data["description"], genre_description)