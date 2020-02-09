from django.db import models

# Create your models here.

class Profile(models.Model):
    profile_photo=models.CharField(max_length=30)
    bio=models.CharField(max_length=30)


class Image(models.Model):
    image=models.CharField(max_length=30)
    image_name=models.CharField(max_length=30)
    image_caption=models.CharField(max_length=30)
    profile=models.ForeignKey(Profile)
    likes=models.IntegerField()
    comments=models.CharField(max_length=30)
    post_time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.image_name




