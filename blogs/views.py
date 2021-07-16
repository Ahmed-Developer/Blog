from django.shortcuts import render, redirect

from .models import BlogPost
from .forms import BlogPostForm

# Create your views here.

def index(request):
    """The home page for Blog."""
    blogposts = BlogPost.objects.order_by('date_added')
    context = {'blogposts': blogposts}
    return render(request, 'blogs/index.html', context)

def new_blog_post(request):
    """Add a new blog post."""
    if request.method != 'POST':
        # No data submitted to create a blank form.
        form = BlogPostForm()
    else:
        # POST data submitted; process data.
        form = BlogPostForm(data=request.POST)
        if form.is_valid():
            form.save()
        return redirect('blogs:index')

    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'blogs/new_blog_post.html', context)
    
def edit_blog_post(request, blog_post_id):
    """Edit an existing blog post."""
    blog_post = BlogPost.objects.get(id=blog_post_id)

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
