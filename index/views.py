import json

from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework import viewsets, permissions

from . import serializers, models

# 分页
class StandardResultsSetPagination(PageNumberPagination):
    page_size = 5# 默认page_size
    page_size_query_param = 'page_size'
    max_page_size = 10000# url里有page_size=10时，默认不能超过当前设置的10000。


# 主页


def index(request):
    return render(request, 'index/index.html', context={})
def head(request):
    return render(request, 'index/head.html', context={})
def news(request):
    return render(request, 'index/news.html', context={})
def newsinfo(request):
    return render(request, 'index/newsinfo.html', context={})
def ability(request):
    return render(request, 'index/ability.html', context={})
def strength(request):
    return render(request, 'index/strength.html', context={})
def about(request):
    return render(request, 'index/about.html', context={})

# 新闻中心
class NewsViewSet(viewsets.ModelViewSet):
    queryset = models.News_center.objects.filter(Q(display_area=1) | Q(display_area=2)).order_by('created_time')
    serializer_class = serializers.NewsSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    pagination_class = StandardResultsSetPagination

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


def newsshow(request):
    queryset1 = models.News_center.objects.filter(display_area=1).first()
    queryset2 = models.News_center.objects.filter(display_area=2)[0]
    queryset3 = models.News_center.objects.filter(display_area=2)[1]
    serializer1 = serializers.NewsSerializer(queryset1)
    serializer2 = serializers.NewsSerializer(queryset2)
    serializer3 = serializers.NewsSerializer(queryset3)
    tmp_dic = {
        'first': serializer1.data,
        'second': serializer2.data,
        'third': serializer3.data,
    }
    return HttpResponse(json.dumps(tmp_dic), content_type='application/json')





# 人力资源、招兵买马
def recruitment(request):
    pass

