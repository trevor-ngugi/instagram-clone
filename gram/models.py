from django.db import models

# Create your models here.
class Image(models.Model):
    image=models.CharField(max_length=30)
    image_name=models.CharField(max_length=30)
    image_caption=models.CharField(max_length=30)
    likes=models.IntegerField()
    comments=models.CharField(max_length=30)
