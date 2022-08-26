from django.shortcuts import render
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


class FilesAPIView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        return Response({'ok'}, status=status.HTTP_200_OK)
