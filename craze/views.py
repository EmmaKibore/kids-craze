from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def home(request):

    return render(request, 'home.html')

def profile(request):
    current_user = request.User
    profile = Profile.objects.all()

    return render(request, 'profile.html', {"profile":profile}) 

def search_results(request):
    if 'business' in request.GET and request.GET["business"]:
        search_term = request.GET.get("business")
        searched_businesses = Business.objects.filter(name=search_term)
        message = f"{search_term}"
        profiles=  Profile.objects.all( )
      
        return render(request, 'search.html',{"message":message,"business": searched_businesses,'profiles':profiles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})


