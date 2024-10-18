from django.urls import path
from . import views

#URLconfのURLパターンを逆引きできるようにするアプリ名
app_name= 'blogapp'

#URLパターンを登録するためのリスト
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('blog-detail/<int:pk>/',
         views.BlogDetail.as_view(),
         name='blog_detail'
         ),
    
    path('science-list/',
         views.ScienceView.as_view(),
         name='science_list'),

    path('dailylife-list/',
         views.DailyLifeView.as_view(),
         name='dailylife_list'),

    path('music-list/',
         views.MusicView.as_view(),
         name='music_list'),
    
    path('contact/',
         views.ContactView.as_view(),
         name='contact'),
    
    
    
]