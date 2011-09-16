from datetime import datetime
from django.utils.html import strip_tags, urlize
from django.contrib import admin
from django.contrib.humanize.templatetags import humanize
from django.contrib.contenttypes.models import ContentType
from django.conf import settings
from models import XXXMODEL_NAMEXXX

def view_on_site(XXXVAR_NAMEXXX):
    '''Return a link to view the XXXVAR_NAMEXXX on site.'''
    type_id = ContentType.objects.get_for_model(XXXMODEL_NAMEXXX).id
    caption = XXXVAR_NAMEXXX.get_absolute_url()
    return '<a href="../../r/%s/%s/">%s</a>' % (type_id, XXXVAR_NAMEXXX.id, caption)
view_on_site.short_description = 'Preview'
view_on_site.allow_tags = True

def content_excerpt(XXXVAR_NAMEXXX, length = 90):
    '''Return the content truncated to the first [length] characters.'''
    text = strip_tags(XXXVAR_NAMEXXX.content)
    return text[:length] + '...' if len(text) > length else text
content_excerpt.short_description = 'Excerpt'

def human_published_on(XXXVAR_NAMEXXX):
    '''Return the humanized version of the published_on date.'''
    return humanize.naturalday(XXXVAR_NAMEXXX.published_on)
human_published_on.short_description = 'Published on'

class XXXMODEL_NAMEXXXAdmin(admin.ModelAdmin):
    # A list of actions to make available on the change list page.
    actions = ['publish_now']
    # Include a date-based drilldown navigation by that field.
    date_hierarchy = 'published_on'
    # A list of field names to exclude from the form.
    exclude = None
    # Control the layout of admin "add" and "change" pages.
    fieldsets = None
    # Control which fields are displayed on the change list page.
    list_display = ('__unicode__', human_published_on,
      content_excerpt, view_on_site, )
    # Activate filters in the right sidebar of the change list page.
    list_filter = ['published_on',]
    # Override model's ordering to specify how objects should be ordered. 
    ordering = None
    # A dictionary mapping field names to the fields it should prepopulate from
    prepopulated_fields = {'slug': ('title',)}
    # A list of field names that will be searchable in the change list page.
    search_fields = ['title','content',]

    class Media:
        relative_paths = ['tinymce/jscripts/tiny_mce/tiny_mce.js', 
          'tinymce_setup/tinymce_setup.js',]
        js = [settings.ADMIN_MEDIA_PREFIX + file for file in relative_paths] 
    
    def publish_now(self, request, queryset):
        rows_updated = queryset.filter(published_on__isnull=True).update(
            published_on=datetime.now())
        if rows_updated == 1: message_bit = "1 XXXSINGULARXXX was"
        else: message_bit = "%s XXXPLURALXXX were" % rows_updated
        self.message_user(request, "%s successfully published." % message_bit)
    publish_now.short_description = "Publish now"

admin.site.register(XXXMODEL_NAMEXXX, XXXMODEL_NAMEXXXAdmin)
