from authentication.api import serializers
from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from users.models import User


class LoginView(generics.GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = serializers.LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
