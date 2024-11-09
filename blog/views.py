from django.shortcuts import render, get_object_or_404
from .models import BlogPost

def post_list(request):
    posts = BlogPost.objects.all().order_by('-created_at')  # Fetch all posts, ordering by newest first
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug, status=1)
    return render(request, 'blog/post_deatil.html', {'post': post})


# Create your views here.
