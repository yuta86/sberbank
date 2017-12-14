from django.shortcuts import render, render_to_response
from django.shortcuts import get_object_or_404
from .models import Banner, Category
from .my_csv import csv_dict_reader
import os


def open(request):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    filename = os.path.join(dir_path, 'banners.csv')
    # Category.objects.all().delete()
    # не очищает таблицу..........не пойму почему
    csv_dict_reader(filename)
    return render(request, 'read_csv/import.html')


def index(request):
    return render(request, 'read_csv/index.html')


def import_csv(request):
    return render(request, 'read_csv/import.html')


def all_category(request):
    category = Category.objects.all()
    print(category)
    return render(request, 'read_csv/list_category.html', {'category': category})


def all_banners(request):
    banners = Banner.objects.all()
    print(banners)
    return render(request, 'read_csv/list_banners.html', {'banners': banners})


def banner(request, Idcategoty):
    print("--------")
    print(Idcategoty)
    category = get_object_or_404(Category, id=Idcategoty)
    print(category)

    # banners_val =Banner.objects.filter(category=category).values()
    # show = banners_val[0]['shows']
    # print (banners)
    # print(banners_val)

    banner = Banner.objects.get(category=category)
    banner.shows = int(banner.shows) - 1
    banner.save()
    print(banner)
    print(banner.shows)
    banners = Banner.objects.filter(category=category)
    print("--------")
    return render(request, 'read_csv/banner.html', {'banners': banners})
