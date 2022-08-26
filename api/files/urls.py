from django.urls import path
from .views import FilesAPIView

app_name = 'files'
urlpatterns = [
    path('', FilesAPIView.as_view()),
]
