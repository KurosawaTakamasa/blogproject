from django.shortcuts import render
from django.views.generic import ListView, DetailView, FormView
from .models import BlogPost
from django.urls import reverse_lazy
from .forms import ContactForm
from django.contrib import messages
from django.core.mail import EmailMessage

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

class ContactView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('blogapp:contact')
    
    def form_valid(self, form):
        
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        title = form.cleaned_data['title']
        message = form.cleaned_data['message']
        
        subject = f'お問合せ: {title}'
        message = \
            f'送信者: {name}\n \
              メールアドレス: {email}\n \
              タイトル: {title}\n \
              メッセージ: {message}'
        
        from_email = 'ymg2465999@stu.o-hara.ac.jp'
        to_list = ['ymg2465999@stu.o-hara.ac.jp']
        
        message = EmailMessage(subject=subject,
                               body=message,
                               from_email=from_email,
                               to = to_list)
        
        message.send()
        
        messages.success(self.request, 
                        'お問合せは正常に送信されました')  
        
        return super().form_valid(form)



