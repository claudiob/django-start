from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext 
from models import Post
from django.conf import settings

def show(request, post_slug):
    post = get_object_or_404(Post, slug=post_slug)
    return render_to_response('posts/show.html', 
        {'post': post}, RequestContext(request))

def index(request):
    posts = Post.objects.published()
    return render_to_response('posts/index.html', 
        {'posts': posts}, RequestContext(request))
