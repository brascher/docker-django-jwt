from django.test import TestCase, Client
from django.urls import resolve, reverse

from rest_framework import status

from ..models import Decade
from ..serializers import DecadeSerializer

class DecadeTest(TestCase):
    """
    Test class for the Decade services
    """

    def setUp(self):
        Decade.objects.create(name="70's")
        Decade.objects.create(name="80's")
        Decade.objects.create(name="00's")

        url = reverse("decades")
        self.response = self.client.get(url)

    def test_decade_all_success_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_decade_contains_all(self):
        decades = Decade.objects.all()
        serializer = DecadeSerializer(decades, many=True)
        self.assertEqual(self.response.data, serializer.data)