from django.contrib import admin

# Register your models here.
from article.models import Article, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_per_page = 20
    search_fields = ('name',)


from django.contrib import messages


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'create_time')
    list_per_page = 10
    autocomplete_fields = ('category',)

    # 第一步 写一个自定义方法

    def my_btn(self, request, queryset):
        # 这里可以做一些自定义的处理，然后处理完毕可以 输出提示信息到前端

        # 比如我这里打印1-100
        for i in range(1, 100):
            print(i)

        messages.add_message(request, messages.SUCCESS, '处理成功')

    # 这里可以设置按钮的名称和图标
    my_btn.short_description = '执行命令'
    my_btn.icon = 'el-icon-check'
    my_btn.type = 'danger'

    # 第二步 设置自定义按钮

    actions = ('my_btn',)
