from django.conf.urls import url

from .views import MissingView, DecadeDetailView, DecadeListView, GenreDetailView, GenreListView

urlpatterns = [
    url(r"^genre/?$", GenreListView.as_view(), name="genres"),
    url(r"^genre/(?P<pk>\d+)/?$", GenreDetailView.as_view(), name="genre"),
    url(r"^decade/?$", DecadeListView.as_view(), name="decades"),
    url(r"^decade/(?P<pk>\d+)/?$", DecadeDetailView.as_view(), name="decade"),
    url(r"^.*", MissingView.as_view(), name="missing"),
]