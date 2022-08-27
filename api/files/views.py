from django.http import JsonResponse
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import File

# Create your views here.


class FilesAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        user = request.user

        files = []
        if(user.is_authenticated):
            files = list(File.objects.filter(user=user).values())
        else:
            files = []

        return JsonResponse(files, safe=False, status=status.HTTP_200_OK)
