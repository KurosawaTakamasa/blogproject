from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import BlogPost

class IndexView(ListView):
    #描画する(レンダリングする) HTMLファイルを指定
    template_name = 'index.html'
    
    #参照するモデルを指定
    #model = BlogPost
    
    queryset = BlogPost.objects.order_by('-posted_at')
    
    paginate_by = 4


class BlogDetail(DetailView):
    #描画する(レンダリングする) HTMLファイルを指定
    template_name = 'post.html'
    
    #参照するモデル(データベース)を設定
    model = BlogPost

class ScienceView(ListView):
    template_name = 'science_list.html'
    
    context_object_name = 'science_records'
    
    queryset = BlogPost.objects.filter(
                category = 'science').order_by('-posted_at')
    
    paginate_by = 2
    
class DailyLifeView(ListView):
    template_name = 'dailylife_list.html'
    
    context_object_name = 'dailylife_records'
    
    queryset = BlogPost.objects.filter(
                category = 'dailylife').order_by('-posted_at')
    
    paginate_by = 2


class MusicView(ListView):
    template_name = 'music_list.html'
    
    context_object_name = 'music_records'
    
    queryset = BlogPost.objects.filter(
                category = 'music').order_by('-posted_at')
    
    paginate_by = 2



