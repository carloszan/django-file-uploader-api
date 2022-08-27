from rest_framework import serializers
from django.contrib.auth import authenticate

from .models import File


class FilesSerializer(serializers.Serializer):
    class Meta:
        model = File
        fields = "__all__"
