from django.conf.urls import url, include
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework.documentation import include_docs_urls

router = DefaultRouter()
router.register(r'news', views.NewsViewSet)

newslist = views.NewsViewSet.as_view({
    'get': 'list',
})

urlpatterns = [
    url(r'^$', views.index),
    url(r'^news/', views.news),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    url(r'^api/docs/', include_docs_urls(title='禾中官网API文档')),
]