from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from django.contrib.auth.models import AbstractUser

# AUTH_USER_MODEL = 'thirdauth.CustomUser'
class CustomUser(AbstractUser): 
    friends_lists = models.TextField()

# class List(models.Model):
#     owner = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True)
#     def get_absolute_url(self):
#         return reverse('view_list', args=[self.id])
#     @staticmethod
#     def create_new(item_firstname, item_lastname, item_zipcode, owner=None):
#         list_ = List.objects.create(owner=owner)
#         # find_nearby_zips(item_zipcode)
#         (cols,rows,p) = query(item_firstname, item_lastname, item_zipcode)
#         Voter.objects.create(firstname=item_firstname, lastname=item_lastname, list=list_)
#     return list_
# class Voter(models.Model):
#     lastname = models.CharField(default='', max_length=100, null=True)
#     firstname = models.CharField(default='', max_length=100, null=True)
#     list = models.ForeignKey(List, default=None)

