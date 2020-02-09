from django.shortcuts import render
from.models import Image

# Create your views here.
def home(request):
    posts=Image.show_images()
    return render(request,'ig/home.html',{'posts':posts})

def search_profile(request):
    if 'profile' in request.GET and request.GET['profile']:
        search_term=request.GET.get('profile')
        results_profiles=Image.search_profile('search_term')
        message=f'{search_term}'
        return render(request,'ig/search.html',{'message':message,'profiles':results_profiles})

    else:
        message='you havent searched for any thing'
        return render(request,'ig/search.html',{'message':message})