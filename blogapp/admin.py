from django.contrib import admin
from .models import BlogPost

#管理サイトにBlogPostを登録する
admin.site.register(BlogPost)