"""This file is used to register models in the admin page"""
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post


# puting my models in the admin page
@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """This class is used to register the Post model in the admin page"""

    summernote_fields = ("content",)
    prepopulated_fields = {"slug": ("title",)}
