from musicapp.models import Song
from django.shortcuts import get_object_or_404
from django.contrib import messages
import random

#Update quantity for single item
def update_song(request):
    postdata = request.POST.copy()
    name = postdata.get('title','')
    description = postdata.get('description','')
    item_id = postdata['item_id']
    song=get_object_or_404(Song, id=item_id)
    if song:
        song.title = name
        song.slug = name
        song.lyrics.content = description
        song.save()

def remove_from_list(request):
    postdata = request.POST.copy()
    item_id = postdata['item_id']
    song=get_object_or_404(Song, id=item_id)
    if song:
        song.delete()
