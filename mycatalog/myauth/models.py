import datetime
import jwt

from rest_framework_jwt.settings import api_settings
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin
)
from django.db import models
from uuid import uuid4

from .managers import UserManager

class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    nick_name = models.CharField(max_length=30, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    jwt_secret = models.UUIDField(default=uuid4)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"

    @property
    def token(self):
        return self.generate_jwt_token()

    def get_full_name(self):
        """
        Formal identifier for the user
        """

        full_name = "{} {}".format(self.first_name, self.last_name)
        return full_name

    def get_short_name(self):
        """
        Short, informal identifier for the user
        """

        short_name = self.nick_name if self.nick_name else self.first_name
        return short_name

    def generate_jwt_token(self):
        """
        Generate a JSON web token that expires in 1 hour.
        """

        dt = datetime.datetime.now() + api_settings.JWT_EXPIRATION_DELTA
        token = jwt.encode({
            "id": self.pk,
            "exp": int(dt.strftime('%s'))
        }, str(self.jwt_secret))

        return token

    def reset_jwt_secret(self):
        """
        Reset the jwt_secret value in order to disable all tokens for the user and
        effectively log them out
        """
        self.jwt_secret = uuid4()

def get_jwt_secret(user_model):
    return user_model.jwt_secret

def get_jwt_email_from_payload_handler(payload):
    return payload.get("email")