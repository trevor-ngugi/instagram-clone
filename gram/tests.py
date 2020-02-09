from django.test import TestCase
from .models import Image,Profile

# Create your tests here.

class ProfileTestClass(TestCase):
    #setup method
    def setUp(self):
        self.trevor=Profile(profile_photo='image',bio='wonderful')

    def test_instance(self):
        self.assertTrue(isinstance(self.trevor,Profile))

    def test_save_method(self):
        self.trevor.save_profile()
        profiles=Profile.objects.all()
        self.assertTrue(len(profiles)>0)

class ImageTestClass(TestCase):
    def setUp(self):

        self.trevor=Profile(profile_photo='image',bio='wonderful')
        self.trevor.save()

        self.post=Image(image='image',image_name='imagename',image_caption='dope',profile=self.trevor,likes=1,comments="dope")

    def test_instance(self):
        self.assertTrue(isinstance(self.post,Image))

    def test_save_method(self):
        self.post.save_image()
        images=Image.objects.all()
        self.assertTrue(len(images)>0)

    def test_delete_method(self):
        self.post.save_image()
        my_obj = Image.objects.get(image='image')
        my_obj.delete()
       