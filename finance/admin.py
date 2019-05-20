from django.contrib import admin
from finance.models import *

from import_export import resources
from import_export.admin import ImportExportModelAdmin, ImportExportActionModelAdmin


class ProxyResource(resources.ModelResource):
    class Meta:
        model = Record


# Register your models here.
@admin.register(Record)
# class RecordAdmin(admin.ModelAdmin):
# class RecordAdmin(ImportExportModelAdmin):
class RecordAdmin(ImportExportActionModelAdmin):

    resource_class = ProxyResource

    list_display = ('id', 'name', 'type', 'money', 'create_date')
    list_per_page = 10
