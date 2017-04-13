from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^api/accounts/', include('apps.accounts.urls')),
]
