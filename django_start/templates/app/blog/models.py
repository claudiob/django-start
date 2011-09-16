from django.conf import settings
from django.db import models
from datetime import datetime
from utils import current_time

class PostManager(models.Manager):
    def published(self):
        return self.filter(published_on__lte=datetime.now())

class Post(models.Model):
    objects         = PostManager()
    title           = models.CharField(max_length=255, help_text=
        "Title of the post (max 255 characters)")
    slug            = models.SlugField(help_text=
        "URL component that identifies the post")
    content         = models.TextField(help_text=
        "Body of the post")
    published_on    = models.DateTimeField(null=True, blank=True, 
      default       = datetime.now(), help_text= 
      "Posts with empty or future date will not appear in the blog.\n" +
      "Current %s time is: %s.<br>" % (settings.TIME_ZONE, current_time()))


    class Meta:
        ordering = ['-published_on',]
        
    def __unicode__(self): 
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('post', (), {'post_slug': self.slug})
    
