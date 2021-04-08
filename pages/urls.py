from django.urls import path
from .views import indexView, categoriesView

urlpatterns = [
    path('', indexView, name='index'),
    path('categories/proetimasia-eikonas/', categoriesView, name='proetimasia_eikonas'),
    path('categories/xuloglupth-eikona/', categoriesView, name='xuloglupth_eikona'),
    path('categories/korniza/', categoriesView, name='korniza'),
]
