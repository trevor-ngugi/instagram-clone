from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.

class Profile(models.Model):
    profile_username=models.CharField(max_length=30)
    profile_pic=models.ImageField(upload_to='profile/',blank=True)
    bio=HTMLField(blank=True)
    no_posts=models.IntegerField(blank=True)
    followers=models.IntegerField(blank=True)
    following=models.IntegerField(blank=True)

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    def __str__(self):
        return self.profile_username

    


class Image(models.Model):
    image=models.ImageField(upload_to='posts/')
    image_name=models.CharField(max_length=30,blank=True, default="Post")
    image_caption=HTMLField(blank=True)
    profile=models.ForeignKey(Profile)
    user=models.ForeignKey(User)
    likes=models.IntegerField(default=0)
    comments=models.CharField(max_length=30,blank=True)
    post_time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.image_name

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def show_images(cls):
        return cls.objects.order_by('post_time')

    @classmethod
    def search_profile(cls,search_term):
        profiles=cls.objects.filter(profile__profile_photo__icontains=search_term)
        return profiles




