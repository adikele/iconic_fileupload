from django.conf.urls import url
from .views import FileView

urlpatterns = [
    url(r'^upload_iconic/$', FileView.as_view(), name='file-upload'),
]
