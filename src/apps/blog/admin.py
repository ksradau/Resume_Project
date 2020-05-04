from django.contrib import admin
from django.contrib.admin import ModelAdmin

from apps.blog.models import BlogPost


@admin.register(BlogPost)
class BlogPostAdminModel(ModelAdmin):
    pass
