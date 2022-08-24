from django.urls import path

from .views import AuthAPIView, LoginAPIView

app_name = 'authentication'
urlpatterns = [
    path('/', AuthAPIView.as_view()),
    path('/login', LoginAPIView.as_view()),
]
