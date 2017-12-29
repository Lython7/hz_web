from django.db import models

# Create your models here.
class News_center(models.Model):
    news_title = models.CharField(max_length=50)
    news_time = models.CharField(max_length=30)
    news_image = models.ImageField()# 路径
    news_content = models.CharField(max_length=3072)
    created_time = models.DateTimeField(auto_now_add=True, editable=False)