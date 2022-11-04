from django.db import models

# Create your models here.
class Artiste(models.Model):
    first_name = models.CharField(max_length=20, verbose_name="First Name")
    last_name = models.CharField(max_length=20, verbose_name="Last Name")
    age = models.IntegerField(verbose_name="Age") 
    
    def __str__ (self):    	
        return self.first_name + " " + self.last_name
    
    
class Song(models.Model):   
    title = models.CharField(max_length=20, verbose_name="Title")  
    slug = models.SlugField(max_length=20, unique=True,help_text='Unique value for product page URL, created from title.')
    artiste_id = models.ForeignKey(Artiste,related_name="song", verbose_name="Artiste" ,on_delete=models.CASCADE, default=None)
    date_released = models.DateTimeField(auto_now_add=True)  
    likes = models.IntegerField(verbose_name="Likes")         
  
    def __str__ (self):    	
        return self.title
    
    
class Lyrics(models.Model):   
    content = models.TextField(max_length=1000, verbose_name="Content")  
    song_id = models.ForeignKey(Song,related_name="lyrics", verbose_name="Song", on_delete=models.CASCADE, default=None) 

    def __str__ (self):    	
        return "lyrics for:" + self.song_id.title