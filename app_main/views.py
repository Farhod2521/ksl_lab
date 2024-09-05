from django.shortcuts import render
from .models import Menu, Page
from django.views.generic import DetailView
from django.shortcuts import get_object_or_404, render


def home(request):
    menu_items = Menu.objects.filter(status=True).order_by('position') 
    return render(request, 'index.html', {'menu_items': menu_items})






def page_view(request, url):
    page = Page.objects.get(url=url)
    menu_items = Menu.objects.filter(status=True).order_by('position') 
    return render(request, 'page.html', {
        'page': page, 
        "menu_items":menu_items,
        
        })