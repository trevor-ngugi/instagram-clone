from django.test import TestCase
from .models import Image,Profile

# Create your tests here.

class ProfileTestClass(TestCase):
    #setup method
    def setUp(self):
        self.trevor=Profile(profile_photo='image',bio='wonderful')

    def test_instance(self):
        self.assertTrue(isinstance(self.trevor,Profile))
