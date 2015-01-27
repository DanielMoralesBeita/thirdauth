from django.db import models
from django.contrib.auth.models import User

#from django.contrib.auth.models import AbstractUser
#class CustomUser(AbstractUser):
#    pass

#http://stackoverflow.com/questions/20976431/get-facebook-user-likes-in-python-social-auth
def get_likes(strategy, details, response, *args, **kwargs):
    if strategy.backend.name == 'facebook':
        likes = strategy.backend.get_json(
            'https://graph.facebook.com/%s/likes' % response['id'],
            params={'access_token': response['access_token']}
        )
        for like in likes['data']:
            pass  # Process and save likes here

class FacebookStatus(models.Model):
    class Meta:
        verbose_name_plural = 'Facebook Statuses'
        ordering = ['publish_timestamp']

    STATUS = (
        ('draft', 'Draft'),
        ('approved', 'Approved'),
    )
    status = models.CharField(max_length=255, 
        choices=STATUS, default=STATUS[0][0])
    publish_timestamp = models.DateTimeField(null=True, blank=True)
    author = models.ForeignKey(User)
    message = models.TextField(max_length=255)
    link = models.URLField(null=True, blank=True)

    def __unicode__(self):
        return self.message

