from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse
from models import Post

class PostsFeed(Feed):
    title = "XXXPROJECT_NAMEXXX &mdash; Posts"
    description = "Latest posts from XXXPROJECT_NAMEXXX"

    def link(self, obj): return reverse('posts')

    def items(self):
        return Post.objects.published()[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content