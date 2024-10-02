from django.urls import path
from . import views

#URLconfのURLパターンを逆引きできるようにするアプリ名
app_name= 'blogapp'

#URLパターンを登録するためのリスト
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
]