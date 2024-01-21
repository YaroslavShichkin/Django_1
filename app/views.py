from django.http import HttpResponse
from django.shortcuts import render, reverse
from datetime import datetime
import os


def home_view(request):
    template_name = 'app/home.html'
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    current_time = datetime.now().strftime("%H часов %M минут %m.%d.%Yг.")
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)


def workdir_view(request):
    path = 'C:\Python Проекты\HW Django\_1. Знакомство с Django\_first_project'
    dirs = os.listdir(path)

    msg = f"Список файлов: {', '.join(dirs)}"
    return HttpResponse(msg)
    # raise NotImplemented