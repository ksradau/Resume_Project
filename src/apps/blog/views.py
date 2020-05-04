from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
from django.views.generic import ListView

from apps.blog.models import BlogPost


class AllBlogPostsView(ListView):  # mix сюда
    template_name = "blog/all_posts.html"
    model = BlogPost


class BlogPostView(DetailView):
    template_name = "blog/post.html"
    model = BlogPost
