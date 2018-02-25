from django.conf.urls import url

from .views import LoginView, LogoutView, RefreshView, RegisterView, UserView

urlpatterns = [
    url(r"^$", UserView.as_view(), name="user"),
    url(r"^register/?$", RegisterView.as_view(), name="register"),
    url(r"^login/?$", LoginView.as_view(), name="login"),
    url(r"^refresh/?$", RefreshView.as_view(), name="refresh"),
    url(r"^logout/?$", LogoutView.as_view(), name="logout"),
]