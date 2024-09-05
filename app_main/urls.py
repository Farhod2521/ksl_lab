from django.urls import path

from .views import home, page_view


urlpatterns  = [
    path("", home, name="home"), 
    path('page/<str:url>/', page_view, name='page_detail'),
]