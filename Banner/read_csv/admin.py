from django.contrib import admin
from .models import Banner, Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Category, CategoryAdmin)

class BannerAdmin(admin.ModelAdmin):
    list_display = ['url', 'shows', 'created', 'updated']

admin.site.register(Banner, BannerAdmin)