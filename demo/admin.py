import datetime

from django.contrib import admin
from django.urls import reverse

from .models import *


# Register your models here.
@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    # 要显示的字段
    list_display = ('id', 'name', 'create_time')

    # 需要搜索的字段
    search_fields = ('name',)

    # 分页显示，一页的数量
    list_per_page = 10

    actions_on_top = True


class ImageInline(admin.TabularInline):
    model = Image


@admin.register(Title)
class TitleAdmin(admin.ModelAdmin):
    # 要显示的字段
    list_display = ('id', 'name')

    # 需要搜索的字段
    search_fields = ('name',)

    # 分页显示，一页的数量
    list_per_page = 10
    inlines = [
        ImageInline,
    ]


class AgeListFilter(admin.SimpleListFilter):
    title = u'最近生日'
    parameter_name = 'ages'

    def lookups(self, request, model_admin):
        return (
            ('0', u'最近7天'),
            ('1', u'最近15天'),
            ('2', u'最近30天'),
        )

    def queryset(self, request, queryset):
        # 当前日期格式
        cur_date = datetime.datetime.now().date()

        if self.value() == '0':
            # 前一天日期
            day = cur_date - datetime.timedelta(days=1)

            return queryset.filter(birthday__gte=day)
        if self.value() == '1':
            day = cur_date - datetime.timedelta(days=15)
            return queryset.filter(birthday__gte=day)
        if self.value() == '2':
            day = cur_date - datetime.timedelta(days=30)
            return queryset.filter(birthday__gte=day)


@admin.register(Employe)
class EmployeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'gender', 'idCard', 'phone', 'birthday', 'department', 'enable', 'create_time')
    search_fields = ('name', 'enable')
    list_per_page = 10
    raw_id_fields = ('department', 'title')
    list_filter = ('department', AgeListFilter)
    # list_filter = (AgeListFilter, 'department', 'create_time', 'birthday', 'time', 'enable', 'gender')

    list_display_links = ('name', 'idCard')

    list_editable = ('department', 'phone', 'birthday', 'enable', 'gender')

    date_hierarchy = 'create_time'
    # 增加自定义按钮
    actions = ['make_copy']

    def make_copy(self, request, queryset):
        ids = request.POST.getlist('_selected_action')
        for id in ids:
            employe = Employe.objects.get(id=id)

            Employe.objects.create(
                name=employe.name,
                idCard=employe.idCard,
                phone=employe.phone,
                birthday=employe.birthday,
                department_id=employe.department_id
            )

    make_copy.short_description = '复制员工'
