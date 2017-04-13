from django.contrib.auth import get_user_model
from rest_framework import permissions
from rest_framework.generics import CreateAPIView

from .serializers import UserSerializer


class RegisterView(CreateAPIView):

    model = get_user_model()
    serializer_class = UserSerializer

    # expose the user registration view to non-authenticated users
    permission_classes = (permissions.AllowAny,)
