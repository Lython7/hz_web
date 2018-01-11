from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import *

# Register your models here.

# userprofile
# class AccountInline(admin.StackedInline):
#     model = Account
#     can_delete = False
#     verbose_name_plural = 'account'

# class UserAdmin(BaseUserAdmin):
#     inlines = (AccountInline,)

# admin.site.unregister(User)
# admin.site.register(User, UserAdmin)


class News_center_Admin(admin.ModelAdmin):
    list_display = ('news_title', 'news_time', 'created_time', 'created_by', )
    search_fields = ('news_title', 'news_time', 'created_time', 'created_by', )
    ordering = ('created_time',)
    list_per_page = 20


class Recruitment_info_Admin(admin.ModelAdmin):
    list_display = ('working_area', 'position_name', 'created_time', 'created_by',)
    search_fields = ('working_area', 'position_name', 'created_time', 'created_by',)
    ordering = ('created_time',)
    list_per_page = 20


admin.site.register(News_center, News_center_Admin)
admin.site.register(Recruitment_info, Recruitment_info_Admin)