from django.conf.urls.defaults import *
from models import Post
from feeds import PostsFeed

urlpatterns = patterns('posts.views',
    (r'^/$', 'index', {}, 'posts'),
    (r'^feed/$', PostsFeed(), {}, 'posts-feed'),
    (r'^(?P<post_slug>.+)/$', 'show', {}, 'post'),
)
