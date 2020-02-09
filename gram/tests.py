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