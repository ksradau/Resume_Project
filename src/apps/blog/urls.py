from django.urls import path

from apps.blog.apps import BlogConfig
from apps.blog.views import AllBlogPostsView
from apps.blog.views import BlogPostView

app_name = BlogConfig.label

urlpatterns = [
    path("", AllBlogPostsView.as_view(), name="all_posts"),
    path("post/<int:pk>/", BlogPostView.as_view(), name="post"),
]
