from django.urls import path

from apps.blog.views import AllBlogPostsView, BlogPostView
from apps.blog.apps import BlogConfig

app_name = BlogConfig.label

urlpatterns = [
    path('', AllBlogPostsView.as_view(), name="all_posts"),
    path('post/<int:pk>/', BlogPostView.as_view(), name="post"),
]