from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url('', include('django.contrib.auth.urls', namespace='auth')),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'thirdauth.views.home', name='home'),
    url(r'^members/', 'thirdauth.views.members', name='members'),
    url('^logout_view/$', 'thirdauth.views.logout_view', name='logout_view'),
)



