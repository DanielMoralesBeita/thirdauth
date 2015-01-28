from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from django.contrib.auth.models import AbstractUser

# AUTH_USER_MODEL = 'thirdauth.CustomUser'
class CustomUser(AbstractUser): 
    friends_lists = models.TextField()
