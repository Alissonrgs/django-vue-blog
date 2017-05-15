from django.conf.urls import url, include
from .views import get_csrf_token


urlpatterns = [
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    url(r'^csrftoken/$', get_csrf_token, name='get_csrftoken'),

    url(r'^(?P<version>(v1))/', include('apps.api.v1.urls'))
]
