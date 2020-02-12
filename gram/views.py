from django.shortcuts import render
from.models import Image
from django.contrib.auth.decorators import login_required
from .forms import PostForm


# Create your views here.
#@login_required(login_url='/accounts/login/')   
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

def new_post(request):
    current_user = request.user

    if request.method == "POST":
        form = PostForm(request.POST)

        if form.is_valid():
            post = comment_form.save(commit=False)
            post.user = current_user
            post.save()
            return redirect("home")

    else:
        form = PostForm()

    return render(request, "ig/new_post.html", context={"form":form})