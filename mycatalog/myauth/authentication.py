import jwt

from django.contrib.auth import get_user_model
from rest_framework import authentication, exceptions
from rest_framework_jwt.settings import api_settings

class MyAuthJwtAuthentication(authentication.BaseAuthentication):
    """
    Custom JWT authentication class for our application
    """

    authentication_header_prefix = "JWT"

    def authenticate(self, request):
        """
        Authenticate the request by finding the JWT in the header and confirming
        it is valid.
        """

        request.user = None

        prefix, token = self.parse_auth_header(request)
        
        if prefix is None or prefix.lower() != self.authentication_header_prefix.lower():
            return None

        return self.auth_token(request, token)

    
    def auth_token(self, request, token):
        """
        Authenticate the token supplied in the request
        """

        try:
            unverified_payload = jwt.decode(token, None, False)
            key = self.get_jwt_secret_key(unverified_payload)
            payload = jwt.decode(token, key)
        except Exception as ex:
            msg = "Invalid authentication"
            raise exceptions.AuthenticationFailed(ex)

        try:
            User = get_user_model()
            user = User.objects.get(pk=payload["id"])
        except User.DoesNotExist:
            msg = "User not found"
            raise exceptions.AuthenticationFailed(msg)

        if not user.is_active:
            msg = "User is not active"
            raise exceptions.AuthenticationFailed(msg)

        return user, token

    def parse_auth_header(self, request):
        """
        Parse the authorization header, if it was supplied in the request.
        """

        if request is None:
            return None,

        auth_header = authentication.get_authorization_header(request).split()

        # Empty auth header means no token provided
        if not auth_header:
            return None, None

        # auth_header should contain ONLY 2 elements; anything different is invalid
        if len(auth_header) == 1 or len(auth_header) > 2:
            return None, None

        prefix = auth_header[0].decode("utf-8")
        token = auth_header[1].decode("utf-8")

        return prefix, token

    def get_jwt_secret_key(self, payload=None):
        """
        This is a utility function copied, and slightly modified, from the 
        django-rest-framework-jwt lib that allows us to get the jwt_secret
        we are storing in the User model for each user from the token.
        """

        if payload is not None:
            User = get_user_model()
            user = User.objects.get(pk=payload["id"])
            key = str(api_settings.JWT_GET_USER_SECRET_KEY(user))
            return key

        return api_settings.JWT_SECRET_KEY
