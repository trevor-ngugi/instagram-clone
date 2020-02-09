from django.shortcuts import render
from.models import Image

# Create your views here.
def home(request):
    posts=Image.show_images()
    return render(request,'ig/home.html',{'posts':posts})