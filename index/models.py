from django.contrib.auth.models import User
from django.db import models
# import time, os

#
# def makepath():
#     basepath = 'index/news_pic/'
#     today = time.localtime()
#     year = str(today.tm_year)
#     mon = str(today.tm_mon)
#     path = basepath+year+'/'+mon+'/'
#     if not os.path.exists(path):
#         try:
#             os.makedirs(path)
#         except:
#             pass
# 新闻中心
class News_center(models.Model):
    choices = (
        (False, '保存'),
        (True, '删除'),
    )
    choices_area = (
        (1,'重磅新闻，页面最上'),
        (2,'次要新闻，页面中间'),
        (3,'其他新闻'),
    )
    news_title = models.CharField(max_length=50, verbose_name='新闻标题', null=False)
    display_area = models.IntegerField(choices=choices_area, default=2)
    news_time = models.DateTimeField(verbose_name='新闻时间', null=False)
    news_image1 = models.ImageField(upload_to='index/news_pic', verbose_name='新闻照片1')# 路径
    news_image2 = models.ImageField(upload_to='index/news_pic', verbose_name='新闻照片2', null=True, blank=True, default='')# 路径
    news_image3 = models.ImageField(upload_to='index/news_pic', verbose_name='新闻照片3', null=True, blank=True, default='')# 路径
    news_image4 = models.ImageField(upload_to='index/news_pic', verbose_name='新闻照片4', null=True, blank=True, default='')# 路径
    news_image5 = models.ImageField(upload_to='index/news_pic', verbose_name='新闻照片5', null=True, blank=True, default='')# 路径
    news_content = models.TextField(max_length=3072, verbose_name='新闻内容', null=False)
    created_time = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='编辑时间', null=False)
    created_by = models.ForeignKey('auth.User', verbose_name='编辑人', null=False, on_delete=True)# 编辑人 editable=False default =当前登录的id, editable=False, default=User
    is_delete = models.BooleanField(choices=choices, default=False, null=False, verbose_name='逻辑删除')

    class Meta:
        # db_table = ''
        ordering = ('created_time', )
        verbose_name = '新闻中心'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.news_title


# 招聘信息
class Recruitment_info(models.Model):
    choices = (
        (False, '保存'),
        (True, '删除'),
    )
    working_area = models.CharField(max_length=20, verbose_name='工作地区', null=False)
    position_name = models.CharField(max_length=20, verbose_name='工作岗位', null=False)
    number = models.IntegerField(verbose_name='招聘人数', null=False)
    experience = models.CharField(max_length=20, verbose_name='工作经验')# 工作经验 可以作为选择模式
    necessary_skills = models.TextField(max_length=1024, verbose_name='技能要求', null=False)# 能力需求
    job_responsibilities = models.TextField(max_length=1024, verbose_name='岗位职责', null=False)
    position_salary = models.CharField(max_length=5, verbose_name='薪资待遇')# 薪资待遇
    created_time = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='编辑时间', null=False)
    created_by = models.ForeignKey(User, verbose_name='编辑人', null=False, on_delete=True)# 编辑人 editable=False default =, editable=False, default=User
    # created_by = models.ForeignKey(User, verbose_name='编辑人', null=False)# 编辑人 editable=False
    is_delete = models.BooleanField(choices=choices, default=False, null=False, verbose_name='逻辑删除')# 逻辑删除

    class Meta:
        # db_table = ''
        ordering = ('created_time', )
        verbose_name = '招聘信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.position_name