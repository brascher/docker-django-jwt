# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

def load_genres_and_decades(app, schema_editore):
    Genre = app.get_model("catalog", "Genre")
    Genre(name="Classical").save()
    Genre(name="Classic Rock").save()
    Genre(name="Hard Rock").save()
    Genre(name="Country").save()
    Genre(name="Heavy Metal").save()
    Genre(name="Alt Rock").save()

    Decade = app.get_model("catalog", "Decade")
    Decade(name="50's").save()
    Decade(name="60's").save()
    Decade(name="70's").save()
    Decade(name="80's").save()
    Decade(name="90's").save()
    Decade(name="00's").save()
    Decade(name="10's").save()

class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_genres_and_decades),
    ]