import jwt

from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login
from django.utils import timezone
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework_jwt.settings import api_settings

from .models import User

class UserSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(
        max_length=255,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )

    class Meta:
        model = User
        fields = ("email", "password", "first_name", "last_name", "nick_name", "token", \
                  "is_active", "date_joined", "last_login",)

        read_only_fields = ("token",)

    def create(self, data):
        """
        Create a new user
        """
        return User.objects.create_user(**data)

    def update(self, instance, data):
        """
        Update an existing user
        """
        password = data.pop("password", None)

        for(key, value) in data.items():
            setattr(instance, key, value)

        if password is not None:
            instance.set_password(password)

        instance.save()

        return instance

class LoginSerializer(serializers.Serializer):

    email = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        """
        Validate the user credentails passed in and issue a token if valid.
        """

        email = data.get("email", None)
        password = data.get("password", None)
            
        if email is None or password is None:
            raise serializers.ValidationError("User credentails are missing")

        user = authenticate(username=email, password=password)

        if user is None:
            raise serializers.ValidationError("User credentails are incorrect")

        if not user.is_active:
            raise serializers.ValidationError("User account has been disabled")

        self.update_last_login(user)
        
        return {
            "email": user.email,
            "token": user.token
        }

    def update_last_login(self, user):
        """
        Update the last_login value for the user
        """
        user.last_login = timezone.now()
        update_last_login(None, user)

class RefreshTokenSerializer(serializers.Serializer):

    token = serializers.CharField(max_length=255)

    def validate(self, data):

        jwt_decode_handler = api_settings.JWT_DECODE_HANDLER

        # print(data.keys())
        token = data.get("token", None)

        try:
            payload = jwt_decode_handler(token)
        except jwt.ExpiredSignature:
            msg = _('Signature has expired.')
            raise serializers.ValidationError(msg)
        except jwt.DecodeError:
            msg = _('Error decoding signature.')
            raise serializers.ValidationError(msg)

        if payload is not None:
            print("IAT: %s" % payload.get("orig_iat", None))
            return { "token": token }
            
        else:
            return { "data": "No token" }
