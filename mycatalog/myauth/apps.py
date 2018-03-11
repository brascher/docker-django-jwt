from django.apps import AppConfig


class MyAuthConfig(AppConfig):
    name = 'myauth'

    def ready(self):
        import myauth.signals
