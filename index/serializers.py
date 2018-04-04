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

            'news_image6',
            'news_image7',
            'news_image8',
            'news_image9',
            'news_image10',

            'news_image11',
            'news_image12',
            'news_image13',
            'news_image14',
            'news_image15',

            'news_image16',
            'news_image17',
            'news_image18',
            'news_image19',
            'news_image20',

            'news_content1',
            'news_content2',
            'news_content3',
            'news_content4',
            'news_content5',

            'news_content6',
            'news_content7',
            'news_content8',
            'news_content9',
            'news_content10',

            'news_content11',
            'news_content12',
            'news_content13',
            'news_content14',
            'news_content15',

            'news_content16',
            'news_content17',
            'news_content18',
            'news_content19',
            'news_content20',
            'created_time',
            'created_by',
            'is_delete',
        )