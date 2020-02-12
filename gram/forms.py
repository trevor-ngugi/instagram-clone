from django import forms
from .models import Image

class PostForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['image_name', 'post_time','profile','user','likes','comments',]
        