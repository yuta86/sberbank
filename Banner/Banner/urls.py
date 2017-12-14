"""Banner URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, re_path
from read_csv import views

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('open/', views.open, name='open'),
    path('list/', views.import_csv, name='list'),
    re_path(r'^all-banners/$', views.all_banners, name='all_banners'),
    re_path(r'^all-category/$', views.all_category, name='all_category'),
    re_path(r'^banners/(?P<Idcategoty>\d+)/$', views.banner, name='banner'),
]
