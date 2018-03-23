from rest_framework import serializers
from . import models

class NewsSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.username')

    class Meta:
        model = models.News_center
        fields = (
            'id',
            'news_title',
            'display_area',
            'news_time',
            'news_image1',
            'news_image2',
            'news_image3',
            'news_image4',
            'news_image5',
            'news_content',
            'created_time',
            'created_by',
            'is_delete',
        )