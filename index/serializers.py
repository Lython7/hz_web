from rest_framework import serializers
from . import models

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.News_center
        fields = (
            'id',
            'news_title',
            'news_time',
            'news_image',
            'news_content',
            'created_time',
            'created_by',
            'is_delete',
        )