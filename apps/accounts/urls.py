from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token

from .views import RegisterView

urlpatterns = [
    url(r'register', RegisterView.as_view(), name='register'),
    url(r'obtain-jwt-token', obtain_jwt_token, name='obtain-jwt-token')
]
