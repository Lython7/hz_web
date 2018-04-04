
from django.conf.urls import url, include

from django.views.static import serve

from hz_web.settings import BASE_DIR
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework.documentation import include_docs_urls

# router = DefaultRouter()
# router.register(r'news', views.NewsViewSet)

newslist = views.NewsViewSet.as_view({
    'get': 'list',
})
newsdetail = views.NewsViewSet.as_view({
    'get': 'retrieve',
})

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^head/', views.head, name='head'),
    url(r'^news/', views.news, name='news'),
    url(r'^newsdetail/', views.newscenter, name='newscenter'),

    url(r'^ability/', views.ability, name='ability'),
    url(r'^strength/', views.strength, name='strength'),
    url(r'^about/', views.about, name='about'),


    url(r'^api/newsinfo/', views.newsshow, name='newsinfo'),
    url(r'^api/newslist/', newslist, name='newslist'),
    url(r'^api/news/(?P<pk>[0-9]+)/', newsdetail, name='newsdetail'),

    # url(r'^api/', include(router.urls)),

    url(r'^media/index/news_pic/(?P<path>.*)', serve, {'document_root': r'media\\index\\news_pic\\'}),

    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    url(r'^api/docs/', include_docs_urls(title='禾中官网API文档')),
]