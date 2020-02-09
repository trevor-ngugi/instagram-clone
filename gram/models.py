from django.db import models

# Create your models here.
class Image(models.Model):
    image=models.CharField(max_length=30)
    image_name=models.CharField(max_length=30)
    image_caption=models.CharField(max_length=30)
    likes=models.IntegerField()
    comments=models.CharField(max_length=30)

    def __str__(self):
        return self.image_name

class Profile(models.Model):
    profile_photo=models.CharField(max_length=30)
    bio=models.CharField(max_length=30)

    
