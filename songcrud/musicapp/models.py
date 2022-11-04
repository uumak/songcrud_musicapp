from django.db import models
from datetime  import datetime
from django.contrib.auth.models import User

# Create your models here.
class Artiste(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField()
    
    def __str__(self):
        return self.first_name
    
class Song(models.Model):
    title = models.CharField(max_length=70)
    date_released = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField()
    artiste_id = models.ForeignKey(Artiste, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
class Lyric(models.Model):
    content = models.CharField(max_length=1000)
    song_id = models.ForeignKey(Song, on_delete=models.CASCADE)
        
    def __str__(self):
        return self.content
