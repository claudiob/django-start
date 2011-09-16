from django.conf import settings
from django.db import models
from datetime import datetime
from utils import current_time

class XXXMODEL_NAMEXXXManager(models.Manager):
    def published(self):
        return self.filter(published_on__lte=datetime.now())

class XXXMODEL_NAMEXXX(models.Model):
    objects         = XXXMODEL_NAMEXXXManager()
    title           = models.CharField(max_length=255, help_text=
        "Title of the XXXSINGULARXXX (max 255 characters)")
    slug            = models.SlugField(help_text=
        "URL component that identifies the XXXSINGULARXXX")
    content         = models.TextField(help_text=
        "Body of the XXXSINGULARXXX")
    published_on    = models.DateTimeField(null=True, blank=True, 
      default       = datetime.now(), help_text= 
      "Any XXXSINGULARXXX with empty or future date will not appear in the blog.\n" +
      "Current %s time is: %s.<br>" % (settings.TIME_ZONE, current_time))


    class Meta:
        ordering = ['-published_on',]
        
    def __unicode__(self): 
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('XXXVAR_NAMEXXX', (), {'XXXVAR_NAMEXXX_slug': self.slug})
    
