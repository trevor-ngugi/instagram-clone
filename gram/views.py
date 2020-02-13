from django.shortcuts import render,redirect
from .models import Image,User,Profile
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from django.http  import HttpResponse,Http404,HttpResponseRedirect



# Create your views here.
#@login_required(login_url='/accounts/login/')   
def home(request):
    posts=Image.show_images()
    return render(request,'ig/home.html',{'posts':posts})

def search_profile(request):
    if 'profile' in request.GET and request.GET["profile"]:
        search_term=request.GET.get("profile")
        results_profiles=Image.search_profile('search_term')
        message=f"{search_term}"
        return render(request,'ig/search.html',{'message':message,'profiles':results_profiles})

    else:
        message='you havent searched for any thing'
        return render(request,'ig/search.html',{'message':message})

def new_post(request):
    current_user = request.user

    if request.method == "POST":
        form = PostForm(request.POST,request.FILES)

        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()
            return redirect("home")

    else:
        form = PostForm()

    return render(request, "ig/new_post.html", context={"form":form})
@login_required
def profile(request, id):
    user = User.objects.get(id=id)
    profile = Profile.objects.get(id=id)
    posts = Post.objects.filter(profile__id=id)[::-1]
    return render(request, "ig/profile.html", context={"user":user,"profile":profile,"posts":posts})