import requests
from django.contrib.auth import authenticate
from rest_framework import serializers


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)
    id = serializers.UUIDField(read_only=True)
    role = serializers.CharField(max_length=128, read_only=True)

    def validate(self, data):
        email = data.get("email", None)
        password = data.get("password", None)

        # Check if a user exists with the given email and password.
        user = authenticate(username=email, password=password)

        if user is None:
            msg = "A user with this email and password was not found."
            raise serializers.ValidationError(msg)

        if not user.is_active:
            msg = "User account has been deactivated."
            raise serializers.ValidationError(msg)

        return {
            "email": user.email,
            "token": user.token,
        }
