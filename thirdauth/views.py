from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.contrib.auth.models import User

from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logout
from socialnetworks.twitter import get_twitter_friends

def home(request):
    context = {}
    template = 'home.html'
    return render(request, template, context)

def members(request):
    context = {}
    if not request.user.is_authenticated():
        return render(request, '/')
    context = {'twitter_friends_list': get_twitter_friends(request)}
    template = 'members.html'
    return render(request, template, context)

def logout_view(request):
    auth_logout(request)
    return redirect('home')



