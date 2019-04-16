from django.contrib import admin
from finance.models import *


# Register your models here.
@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'type', 'money', 'create_date')
    list_per_page = 10
