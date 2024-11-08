from django.shortcuts import render
from .models import BlogPost

def post_list(request):
    posts = BlogPost.objects.all().order_by('-created_at')  # Fetch all posts, ordering by newest first
    return render(request, 'blog/post_list.html', {'posts': posts})

# Create your views here.
