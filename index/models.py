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

    newslist_img = models.ImageField(upload_to='index/news_pic', verbose_name='新闻列表小图', null=False)# 路径

    news_image1 = models.ImageField(upload_to='index/news_pic', verbose_name='新闻图片段落1上', null=True, blank=True, default='')# 路径
    news_content1 = models.TextField(max_length=1024, verbose_name='新闻内容段落1', null=False)

    news_image2 = models.ImageField(upload_to='index/news_pic', verbose_name='新闻图片段落2上', null=True, blank=True, default='')# 路径
    news_content2 = models.TextField(max_length=1024, verbose_name='新闻内容段落2', null=True, blank=True, default='')

    news_image3 = models.ImageField(upload_to='index/news_pic', verbose_name='新闻图片段落3上', null=True, blank=True, default='')# 路径
    news_content3 = models.TextField(max_length=1024, verbose_name='新闻内容段落3', null=True, blank=True, default='')

    news_image4 = models.ImageField(upload_to='index/news_pic', verbose_name='新闻图片段落4上', null=True, blank=True, default='')# 路径
    news_content4 = models.TextField(max_length=1024, verbose_name='新闻内容段落4', null=True, blank=True, default='')

    news_image5 = models.ImageField(upload_to='index/news_pic', verbose_name='新闻图片段落5上', null=True, blank=True, default='')# 路径
    news_content5 = models.TextField(max_length=1024, verbose_name='新闻内容段落5', null=True, blank=True, default='')

    news_image6 = models.ImageField(upload_to='index/news_pic', verbose_name='新闻图片段落6上', null=True, blank=True, default='')# 路径
    news_content6 = models.TextField(max_length=1024, verbose_name='新闻内容段落6', null=True, blank=True, default='')

    news_image7 = models.ImageField(upload_to='index/news_pic', verbose_name='新闻图片段落7上', null=True, blank=True, default='')# 路径
    news_content7 = models.TextField(max_length=1024, verbose_name='新闻内容段落7', null=True, blank=True, default='')

    news_image8 = models.ImageField(upload_to='index/news_pic', verbose_name='新闻图片段落8上', null=True, blank=True, default='')# 路径
    news_content8 = models.TextField(max_length=1024, verbose_name='新闻内容段落8', null=True, blank=True, default='')

    news_image9 = models.ImageField(upload_to='index/news_pic', verbose_name='新闻图片段落9上', null=True, blank=True, default='')# 路径
    news_content9 = models.TextField(max_length=1024, verbose_name='新闻内容段落9', null=True, blank=True, default='')

    news_image10 = models.ImageField(upload_to='index/news_pic', verbose_name='新闻图片段落10上', null=True, blank=True, default='')# 路径
    news_content10 = models.TextField(max_length=1024, verbose_name='新闻内容段落10', null=True, blank=True, default='')

    news_image11 = models.ImageField(upload_to='index/news_pic', verbose_name='新闻图片段落11上', null=True, blank=True, default='')# 路径
    news_content11 = models.TextField(max_length=1024, verbose_name='新闻内容段落11', null=True, blank=True, default='')

    news_image12 = models.ImageField(upload_to='index/news_pic', verbose_name='新闻图片段落12上', null=True, blank=True, default='')# 路径
    news_content12 = models.TextField(max_length=1024, verbose_name='新闻内容段落12', null=True, blank=True, default='')

    news_image13 = models.ImageField(upload_to='index/news_pic', verbose_name='新闻图片段落13上', null=True, blank=True, default='')# 路径
    news_content13 = models.TextField(max_length=1024, verbose_name='新闻内容段落13', null=True, blank=True, default='')

    news_image14 = models.ImageField(upload_to='index/news_pic', verbose_name='新闻图片段落14上', null=True, blank=True, default='')# 路径
    news_content14 = models.TextField(max_length=1024, verbose_name='新闻内容段落14', null=True, blank=True, default='')

    news_image15 = models.ImageField(upload_to='index/news_pic', verbose_name='新闻图片段落15上', null=True, blank=True, default='')# 路径
    news_content15 = models.TextField(max_length=1024, verbose_name='新闻内容段落15', null=True, blank=True, default='')

    news_image16 = models.ImageField(upload_to='index/news_pic', verbose_name='新闻图片段落16上', null=True, blank=True, default='')# 路径
    news_content16 = models.TextField(max_length=1024, verbose_name='新闻内容段落16', null=True, blank=True, default='')

    news_image17 = models.ImageField(upload_to='index/news_pic', verbose_name='新闻图片段落17上', null=True, blank=True, default='')# 路径
    news_content17 = models.TextField(max_length=1024, verbose_name='新闻内容段落17', null=True, blank=True, default='')

    news_image18 = models.ImageField(upload_to='index/news_pic', verbose_name='新闻图片段落18上', null=True, blank=True, default='')# 路径
    news_content18 = models.TextField(max_length=1024, verbose_name='新闻内容段落18', null=True, blank=True, default='')

    news_image19 = models.ImageField(upload_to='index/news_pic', verbose_name='新闻图片段落19上', null=True, blank=True, default='')# 路径
    news_content19 = models.TextField(max_length=1024, verbose_name='新闻内容段落19', null=True, blank=True, default='')

    news_image20 = models.ImageField(upload_to='index/news_pic', verbose_name='新闻图片段落20上', null=True, blank=True, default='')# 路径
    news_content20 = models.TextField(max_length=1024, verbose_name='新闻内容段落20', null=True, blank=True, default='')



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