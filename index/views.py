from django.shortcuts import render, render_to_response
from rest_framework.decorators import api_view
from rest_framework.response import Response

from . import serializers, models

# 主页
def index(request):
    return render(request, 'index/index.html', context={})

# 新闻中心
@api_view(['GET', ])
def news_list(request):
    if request.method == "GET":
        queryset = models.News_center.objects.all()
        serializer = serializers.NewsSerializer(queryset, many=True)
        return Response(serializer.data)

# 人力资源、招兵买马
def recruitment(request):
    pass

