from django.db import models

# Create your models here.
class Artiste(models.Model):
    first_name = models.CharField(max_length=20, verbose_name="First Name")
    last_name = models.TextField(max_length=1000, verbose_name="Last Name")
    age = models.IntegerField(verbose_name="Age") 
    
    def __str__ (self):    	
        return self.first_name + " " + last_name
    
    
class Song(models.Model):   
    title = models.CharField(max_length=50, verbose_name="Title")  
    artiste_id = models.CharField(max_length=20, verbose_name="Artiste ID")
    date_released = models.DateField(auto_now_add=True)  
    likes = models.IntegerField(verbose_name="Likes")    
    artiste = models.ForeignKey(Artiste, verbose_name="Artiste" ,on_delete=models.CASCADE, default=None)    
  
    def __str__ (self):    	
        return self.title
    
    
class Lyrics(models.Model):   
    content = models.CharField(max_length=50, verbose_name="Content")  
    song_id = models.CharField(max_length=20, verbose_name="Song ID)
    song = models.ForeignKey(Song, verbose_name="Song", on_delete=models.CASCADE, default=None)    

    def __str__ (self):    	
        return self.song
