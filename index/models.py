from django.contrib.auth.models import User
from django.db import models

# 新闻中心
class News_center(models.Model):
    choices = (
        (False, '保存'),
        (True, '删除'),
    )
    news_title = models.CharField(max_length=50, verbose_name='新闻标题', null=False)
    news_time = models.DateTimeField(verbose_name='新闻时间', null=False)
    news_image = models.ImageField(upload_to='index/news_pic', verbose_name='新闻照片', null=False)# 路径
    news_content = models.TextField(max_length=3072, verbose_name='新闻内容', null=False)
    created_time = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='编辑时间', null=False)
    created_by = models.ForeignKey('auth.User', verbose_name='编辑人', null=False)# 编辑人 editable=False default =当前登录的id
    is_delete = models.BooleanField(choices=choices, default=False, null=False, verbose_name='逻辑删除')

    class Meta:
        # db_table = ''
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
    created_by = models.ForeignKey(User, verbose_name='编辑人', null=False)# 编辑人 editable=False default =
    # created_by = models.ForeignKey(User, verbose_name='编辑人', null=False)# 编辑人 editable=False
    is_delete = models.BooleanField(choices=choices, default=False, null=False, verbose_name='逻辑删除')# 逻辑删除

    class Meta:
        # db_table = ''
        verbose_name = '招聘信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.position_name