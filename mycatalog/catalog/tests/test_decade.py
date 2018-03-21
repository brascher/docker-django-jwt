from django.test import RequestFactory, TestCase, Client
from django.urls import resolve

from ..models import Decade
from ..serializers import DecadeSerializer
from ..views import DecadeDetailView, DecadeListView

class DecadeTest(TestCase):
    """
    Test class for the Decade model, serializer, and views
    """

    def setUp(self):
        self.request_factory = RequestFactory()
        self.name = "30's"

    def create_decade(self):
        return Decade.objects.create(name=self.name)

    def test_decade_create(self):
        """
        Simple model test
        """
        new_decade = self.create_decade()
        self.assertTrue(isinstance(new_decade, Decade))
        self.assertEqual(new_decade.name, self.name)

    def test_decade_list_success_status_code(self):
        """
        Decades list status code is correct
        """
        request = self.request_factory.get("/api/v1/decade/")
        response = DecadeListView.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_decade_detail_success_status_code(self):
        """
        Decade detail status code is correct
        """
        request = self.request_factory.get("/api/v1/decade/1/")
        response = DecadeDetailView.as_view()(request, pk=1)
        self.assertEqual(response.status_code, 200)

    def test_decade_not_found_status(self):
        """
        Decade not found status code is correct
        """
        request = self.request_factory.get("/api/v1/decade/99/")
        response = DecadeDetailView.as_view()(request, pk=99)
        self.assertEquals(response.status_code, 404)

    def test_decade_url_resolves_decade_list_view(self):
        """
        Decades list url calls the correct view
        """
        view = resolve("/api/v1/decade/")
        self.assertEquals(view.view_name, "decades")

    def test_decade_with_id_url_resolves_decade_detail_view(self):
        """
        Decade detail url calls the correct view
        """
        view = resolve("/api/v1/decade/1/")
        self.assertEquals(view.view_name, "decade")

    def test_decade_serializer_fields(self):
        """
        Decade serializer returns the correct fields
        """
        expected_fields = ["id", "name", "updated_at"]
        test_decade = Decade.objects.get(pk=1)
        serializer = DecadeSerializer(test_decade)
        self.assertCountEqual(serializer.data.keys(), expected_fields)

    def test_decade_serializer_content(self):
        """
        Decade serializer returns the correct data
        """
        decade_pk = 1
        decade_name = "50's"
        test_decade = Decade.objects.get(pk=decade_pk)
        serializer = DecadeSerializer(test_decade)
        self.assertEqual(serializer.data["id"], decade_pk)
        self.assertEqual(serializer.data["name"], decade_name)