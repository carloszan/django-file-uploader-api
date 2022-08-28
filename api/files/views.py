from django.http import JsonResponse
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import File
from django.utils import timezone

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

    def post(self, request):
        file_name = request.data["name"]

        try:
            file = File(name=file_name, type="jpg",
                        file_url="abc", pub_date=timezone.now(), user=request.user)

            file.save()
            return Response({'id': '630b5e07c6997747ea7dc97b'}, status=201)
        except:
            return Response(status=403)
