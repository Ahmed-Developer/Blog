"""Defines URL patterns for blogs."""

from django.urls import path

from . import views

app_name = 'blogs'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Page for adding a new blog post
    path('new_blog_post/', views.new_blog_post, name='new_blog_post'),
    # Page for editing a blog post
    path('edit_blog_post/<int:blog_post_id>/', views.edit_blog_post, name='edit_blog_post'),
]
