import markdown
from django.db import models

from mdeditor.fields import MDTextField


class Category(models.Model):
    name = models.CharField(max_length=128, verbose_name='分类名', unique=True, db_index=True)

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = '分类管理'

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=128, verbose_name='标题', unique=True, db_index=True)
    content_raw = MDTextField(verbose_name='原始内容')
    content_render = models.TextField(verbose_name='呈现内容', null=True, blank=True)

    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=False, null=True, verbose_name='分类',
                                 db_index=True)

    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)

    def save(self, *args, **kwargs):
        # 将Markdown格式 转为html，页面上显示
        self.content_render = markdown.markdown(self.content_raw, extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            'markdown.extensions.toc',
        ])
        super(Article, self).save(*args, **kwargs)

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = '文章管理'

    def __str__(self):
        return self.title
