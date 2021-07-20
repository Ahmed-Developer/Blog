from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import BlogPost
from .forms import BlogPostForm

# Create your views here.

def index(request):
    """The home page for Blog."""
    blogposts = BlogPost.objects.order_by('date_added')
    context = {'blogposts': blogposts}
    return render(request, 'blogs/index.html', context)

@login_required
def new_blog_post(request):
    """Add a new blog post."""
    if request.method != 'POST':
        # No data submitted to create a blank form.
        form = BlogPostForm()
    else:
        # POST data submitted; process data.
        form = BlogPostForm(data=request.POST)
        if form.is_valid():
            new_blog_post = form.save(commit=False)
            new_blog_post.owner = request.user
            new_blog_post.save()
            return redirect('blogs:index')

    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'blogs/new_blog_post.html', context)

@login_required    
def edit_blog_post(request, blog_post_id):
    """Edit an existing blog post."""
    blog_post = BlogPost.objects.get(id=blog_post_id)
    if blog_post.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # Initial request; pre-fill form with the current entry.
        form = BlogPostForm(instance=blog_post)
    else:
        # POST data submitted; process data.
        form = BlogPostForm(instance=blog_post, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:index')

    context = {'blog_post': blog_post, 'form': form}
    return render(request, 'blogs/edit_blog_post.html', context)
