from rest_framework import serializers

from .models import Genre, Decade

class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ("id", "name", "description", "updated_at")

class DecadeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Decade
        fields = ("id", "name", "updated_at")