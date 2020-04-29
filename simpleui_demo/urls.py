"""simpleui_demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

admin.site.site_title = '管理后台'
admin.site.site_header = '员工管理后台'

urlpatterns = [
                  # 配置admindoc
                  url(r'doc/', include('django.contrib.admindocs.urls'), name='doc'),
                  path('', admin.site.urls),
                  url(r'mdeditor/', include('mdeditor.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
