from django.conf.urls import url 
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.index, name = 'home'),
    url(r'^projects/(\d+)', views.projects, name='projects'),
    url(r'^profile/(?P<username>\w+)', views.profile, name='profile'),
    url(r'^uploads/', views.post_site, name='post_site'),
    url(r'^search/', views.search_results, name='search_results')
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)