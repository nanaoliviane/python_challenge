from django.shortcuts import render, get_object_or_404, redirect
from .models import BlogPost
from .forms import BlogPostForm
from django.utils import timezone

def post_list(request):
    posts = BlogPost.objects.all().order_by('-created_at')  # Fetch all posts, ordering by newest first
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug, status=1)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = BlogPostForm(request.POST)
        if form.is_valid():
            BlogPost = form.save(commmit=False)
            BlogPost.author = request.user
            BlogPost.published_date = timezone.now()
            BlogPost.save()
            return redirect('post_detail', pk=BlogPost.pk)
    else:
        form = BlogPostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    if request.method == "POST":
        form = BlogPostForm(request.POST, instance=post)
        if  form.is_valid():
            BlogPost = form.save(commit= False)
            BlogPost.author = request.user
            BlogPost.published_date = timezone.now()
            BlogPost.save()
            return redirect('post_detail', pk=BlogPost.pk)
    else:
        form = BlogPostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})