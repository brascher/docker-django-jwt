from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

class Decade(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

class Artist(models.Model):
    name = models.CharField(max_length=50)
    notes = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

class Song(models.Model):
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT, related_name="genre")
    decade = models.ForeignKey(Decade, on_delete=models.PROTECT, related_name="decade")
    artist = models.ForeignKey(Artist, on_delete=models.PROTECT, related_name="artist")
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=255, blank=True)
    # length ???
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
