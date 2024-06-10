from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from users.api.serializers import UserSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from users.models import User

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

