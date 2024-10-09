from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import BlogPost

class IndexView(ListView):
    #描画する(レンダリングする) HTMLファイルを指定
    template_name = 'index.html'
    
    #参照するモデルを指定
    #model = BlogPost
    
    queryset = BlogPost.objects.order_by('-posted_at')


class BlogDetail(DetailView):
    #描画する(レンダリングする) HTMLファイルを指定
    template_name = 'post.html'
    
    #参照するモデル(データベース)を設定
    model = BlogPost


