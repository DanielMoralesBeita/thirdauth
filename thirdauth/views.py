from django.shortcuts import render_to_response
from django.template.context import RequestContext

def home(request):
   context = RequestContext(request,
                           {'request': request,
                            'user': request.user})
   return render_to_response('home.html',
                             context_instance=context)

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
