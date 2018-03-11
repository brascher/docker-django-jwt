from django.test import TestCase, Client
from django.urls import reverse

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

        self.response_all = self.client.get("/api/v1/decade/")

    def test_decade_all_success_status_code(self):
        self.assertEqual(self.response_all.status_code, 200)

    def test_decade_contains_all(self):
        decades = Decade.objects.all()
        serializer = DecadeSerializer(decades, many=True)
        self.assertEqual(self.response_all.data, serializer.data)