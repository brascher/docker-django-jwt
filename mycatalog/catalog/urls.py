from django.conf.urls import url

from .views import DecadeView, GenreView

urlpatterns = [
    url(r"^genre/?$", GenreView.as_view(), name="genres"),
    url(r"^decade/?$", DecadeView.as_view(), name="decades"),
]