from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.contrib.auth.models import User

# def home(request):
#    context = RequestContext(request,
#                            {'request': request,
#                             'user': request.user})
# #   get_google_friends(request)
# #   get_facebook_friends(request)
#    return render_to_response('home.html',
#                              context_instance=context)

from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logout

def home(request):
    context = {}
    template = 'home.html'
    return render(request, template, context)

def members(request):
    context = {}
    template = 'members.html'
    return render(request, template, context)

#{% url "socialauth_disconnect" "backend-name" %}

def logout_view(request):
    auth_logout(request)
    return redirect('home')

import requests
import json
import urllib
#http://axiacore.com/blog/how-retrieve-facebook-extra-info-from-django/
def get_facebook_friends(request):
   social_user = ''
   try:
      social_user = request.user.social_auth.filter(provider='facebook',).first()
   except: 
      pass
   if social_user:
      url = u'<a href="https://graph.facebook.com/{0}/">https://graph.facebook.com/{0}/</a>' \
            u'friends?fields=id,name,location,picture' \
            u'&access_token={1}'.format(
         social_user.uid,
         social_user.extra_data['access_token'],
         )
      #request = urllib.request(url)
      friends = json.loads(urllib.urlopen(url).read()).get('data')
      for friend in friends:
         location = friend.get('location')
         print(location)
   else:
      print('no facebook provider?')
   # do something



import requests
import json
def get_google_friends(request):
   print(User.objects.filter())
   user = User.objects.filter()
#   user = User.objects.get()
   user = user[3]
   social = user.social_auth.get(provider='google-oauth2')
   response = requests.get(
      'https://www.googleapis.com/plus/v1/people/me/people/visible',
      params={'access_token': social.extra_data['access_token']}
      )
   friends = response.json()#['displayName']#'items'
   print(friends.keys())#['totalItems'])

#Let’s say we are interested in storing the user profile link, the gender and the timezone in our Profile
# def save_profile(backend, user, response, *args, **kwargs):
#     if backend.name == 'facebook':
#         profile = user.get_profile()
#         if profile is None:
#             profile = Profile(user_id=user.id)
#         profile.gender = response.get('gender')
#         profile.link = response.get('link')
#         profile.timezone = response.get('timezone')
#         profile.save()
