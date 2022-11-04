from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from musicapp.models import Artiste, Song, Lyrics
from musicapp import action
from songcrud import settings

# Create your views here.

def home(request):
    #getting the total number of our tasks
    
    page_title='Home'
    songs = Song.objects.all()
    artiste = Artiste.objects.all()
    total_song = Song.objects.all().count()
    total_artiste = Artiste.objects.all().count()

    #set the test cookie on our first GET request
    request.session.set_test_cookie()
    return render(request,'index.html',{'songs':songs,'artiste':artiste,'total_artiste':total_artiste,'total_song':total_song,'page_title':page_title})

def show_song(request, slug):
    song=Song.objects.get(slug=slug)
    page_title = song.title
    #getting related products
    songs = Song.objects.filter(artiste_id=song.artiste_id)
    lyrics = Lyrics.objects.filter(song_id=song)
    # need to evaluate the HTTP method
    if request.method=="POST":
        #add to action...create the bound form
        postdata = request.POST.copy()
        if postdata['submit'] == 'Remove':
            action.remove_from_list(request)
            return redirect('musicapp:home')
        if postdata['submit'] == 'Update':
            action.update_song(request)
            return redirect('musicapp:home')
    return render(request,'song.html',{'lyrics':lyrics,'songs':songs,'song':song,'page_title':page_title})

def show_artiste(request, first_name):
    artiste=Artiste.objects.get(first_name=first_name)
    page_title = artiste.first_name
    #getting related products
    songs = Song.objects.filter(artiste_id=artiste)
    return render(request,'artiste.html',{'songs':songs,'artiste':artiste,'page_title':page_title})
