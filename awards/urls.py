from django.conf.urls import url 
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'home'),
    url(r'^projects/(\d+)', views.projects, name='projects'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)