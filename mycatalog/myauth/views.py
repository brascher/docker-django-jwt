import datetime

from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_jwt.serializers import RefreshJSONWebTokenSerializer
from uuid import uuid4

from .models import User
from .renderers import UserRenderer
from .serializers import LoginSerializer, UserSerializer

# /user/register/ service; POST only
class RegisterView(APIView):

    permission_classes = (AllowAny,)
    renderer_classes = (UserRenderer,)
    serializer_class = UserSerializer

    def post(self, request):

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

# /user/login/ view; POST only
class LoginView(APIView):

    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer  

    def post(self, request):
        
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# /user/login/ view; POST only
class RefreshView(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = RefreshJSONWebTokenSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# /user/logout/ view; POST only
class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        
        user = request.user
        user.jwt_secret = uuid4()
        user.save()
        return Response(status=status.HTTP_403_FORBIDDEN)

# /user/ view; GET, POST
class UserView(APIView):
    permission_classes = (IsAuthenticated,)
    renderer_classes = (UserRenderer,)
    serializer_class = UserSerializer

    def get(self, request):

        serializer = self.serializer_class(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        
        serializer = self.serializer_class(request.user,
                                           data=request.data.get("user", {}),
                                           partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
