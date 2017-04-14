from django.conf.urls import url, include


urlpatterns = [
    url(r'', include('apps.core.urls')),
    url(r'^api/accounts/', include('apps.accounts.urls')),
]
