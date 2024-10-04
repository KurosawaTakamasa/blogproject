from django.shortcuts import render
from django.views.generic import ListView
from .models import BlogPost

class IndexView(ListView):
    #描画する(レンダリングする) HTMLファイルを指定
    template_name = 'index.html'
    
    #参照するモデルを指定
    #model = BlogPost
    
    queryset = BlogPost.objects.order_by('-posted_at')


