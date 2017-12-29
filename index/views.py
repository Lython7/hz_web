from django.shortcuts import render, render_to_response

# 主页
def index(request):
    return render(request, 'index/index.html', context={})

# 新闻中心
def news_center(request):
    pass

# 人力资源、招兵买马
def recruitment(request):
    pass

