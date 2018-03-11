from django.utils import timezone
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import Genre, Decade

class GenreSerializer(serializers.ModelSerializer):

    name = serializers.CharField(
        max_length=50,
        required=True,
        validators=[UniqueValidator(queryset=Genre.objects.all())]
    )

    class Meta:
        model = Genre
        fields = ("id", "name", "description", "updated_at")

        read_only_fields = ("id", "updated_at",)

    def create(self, data):
        """
        Create a new genre
        """
        return Genre.objects.create(**data)

    def update(self, instance, data):
        """
        Update an existing genre
        """

        for (key, value) in data.items():
            setattr(instance, key, value)

        instance.updated_at = timezone.now()
        instance.save()

        return instance

class DecadeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Decade
        fields = ("id", "name", "updated_at")

        read_only_fields = ("id", "updated_at",)