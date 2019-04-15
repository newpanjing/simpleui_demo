from django.contrib import admin
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


@admin.register(Employe)
class EmployeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'gender', 'idCard', 'phone', 'birthday', 'department', 'enable', 'create_time')
    search_fields = ('name', 'enable')
    list_per_page = 10

    list_filter = ('department', 'create_time', 'birthday', 'time', 'enable', 'gender')

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
