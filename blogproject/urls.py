from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    #http(s)://ホスト名/へのアクセスはblogappの
    #urls.pyを呼び出す
    path('', include('blogapp.urls') ),
]
