from django.test import TestCase
from .models import Image,Profile,User

# Create your tests here.

class ProfileTestClass(TestCase):
    #setup method
    def setUp(self):
        self.user= User(first_name="trevor", last_name='ngugi',username="t.ngugi", email="ngugi@gmail.com",)
        self.user.save()

        self.trevor = Profile(profile_username=self.user, bio="None",no_posts='0',followers=0, following=0,)
    def test_instance(self):
        self.assertTrue(isinstance(self.trevor,Profile))

    def test_save_method(self):
        self.trevor.save_profile()
        profiles=Profile.objects.all()
        self.assertTrue(len(profiles)>0)

    def test_delete_method(self):
        self.trevor.save_profile()
        my_obj = Profile.objects.get(profile_username='t.ngugi')
        my_obj.delete()

class ImageTestClass(TestCase):
    def setUp(self):
        self.user= User(first_name="trevor", last_name='ngugi',username="t.ngugi", email="ngugi@gmail.com",)
        self.user.save()

        self.trevor = Profile(profile_username=self.user, bio="None",no_posts='0',followers=0, following=0,)
        self.trevor.save()

        self.post=Image(image_name='post',image_caption='dope',profile=self.trevor,user=self.user, comments="dope")


    def test_instance(self):
        self.assertTrue(isinstance(self.post,Image))

    def test_save_method(self):
        self.post.save_image()
        images=Image.objects.all()
        self.assertTrue(len(images)>0)

    def test_delete_method(self):
        self.post.save_image()
        my_obj = Image.objects.get(image_caption='dope')
        my_obj.delete()

class UserTestClass(TestCase):
    def setUp(self):
        self.user = User(first_name="trevor", last_name="ngugi", username="t.ngugi", email="ngugi@gmail.com",)

    def test_instance(self):
        self.assertTrue(isinstance(self.user, User))
       