from ast import pattern
from django.contrib import admin
admin.autodiscover()
from django.urls import path, re_path
from . import views

app_name = 'musicapp'

urlpatterns = [
    re_path(r'^$', views.home, name='home'),
    re_path(r'^song-details/(?P<slug>[-\w]+)/$',views.show_song, name='song_detail'),
    re_path(r'^artiste-details/(?P<first_name>[-\w]+)/$',views.show_artiste, name='artiste_detail'),
]
