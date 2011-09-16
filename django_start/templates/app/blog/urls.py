from django.conf.urls.defaults import *
from models import Post
from feeds import PostsFeed

urlpatterns = patterns('posts.views',
    (r'^/$', 'index', {}, 'posts'),
    (r'^(?P<post_slug>.+)/$', 'show', {}, 'post'),
    (r'^feed/$', PostsFeed(), {}, 'posts-feed'),
)
