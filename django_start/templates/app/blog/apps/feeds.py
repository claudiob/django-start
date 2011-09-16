from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse
from models import XXXMODEL_NAMEXXX

class XXXMODEL_NAMEXXXFeed(Feed):
    title = "Latest XXXPLURALXXX"
    description = "Latest XXXPLURALXXX"

    def link(self, obj): return reverse('XXXVAR_NAMEXXXs')

    def items(self):
        return XXXMODEL_NAMEXXX.objects.published.order_by('-published_on')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content