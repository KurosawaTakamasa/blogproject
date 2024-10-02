from django.shortcuts import render
from django.views.generic.base import TemplateView

class IndexView(TemplateView):
    #描画する(レンダリングする) HTMLファイルを指定
    template_name = 'index.html'

