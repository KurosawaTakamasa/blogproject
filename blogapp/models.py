from django.db import models

class BlogPost(models.Model):
    #タイトル用フィールド
    title = models.CharField(max_length=200,
                             verbose_name='タイトル')
    
    #本文用のフィールド
    content = models.TextField(verbose_name='本文')
    
    #投稿日時のフィールド
    posted_at = models.DateTimeField(verbose_name='投稿日時',
                                     auto_now_add=True)
    
    #カテゴリ用のフィールド
    category = models.CharField(max_length=50,
                                verbose_name='カテゴリ',
                                choices=(('science','科学のこと' ),
                                         ('dailylife', '日常生活のこと'),
                                         ('music', '音楽のこと'))
                                )
    
    def __str__(self):
        return self.title
    
