from django.conf.urls import  url
from . import views

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r"uploadFile", views.uploadFile, name = "uploadFile"),
]


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root = settings.MEDIA_ROOT
    )