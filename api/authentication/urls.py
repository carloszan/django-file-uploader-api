from django.urls import path

from .views import AuthAPIView

app_name = 'authentication'
urlpatterns = [
    path('/', AuthAPIView.as_view()),
]
