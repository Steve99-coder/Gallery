
from django.conf.urls import url
from django.urls import path,re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',views.image,name = 'image'),
    path('search/', views.search_results, name='search_results'),
    url(r'^location/(?P<location>\w+)/', views.location, name='location'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)