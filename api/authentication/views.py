from rest_framework import status
from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.


class AuthAPIView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        return Response({'ok'}, status=status.HTTP_200_OK)