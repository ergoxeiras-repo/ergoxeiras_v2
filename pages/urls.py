from django.urls import path
from .views import indexView, categoriesView

urlpatterns = [
    path('', indexView, name='index'),
    path('categories/proetimasia-eikonas/', categoriesView, name='proetimasia_eikonas'),
    path('categories/xuloglupth-eikona/', categoriesView, name='xuloglupth_eikona'),
    path('categories/korniza/', categoriesView, name='korniza'),
    path('categories/forhth-eikona/', categoriesView, name='forhth_eikona'),
    path('categories/kytia/', categoriesView, name='kytia'),
    path('categories/leipsanothikes/', categoriesView, name='leipsanothikes'),
    path('categories/byzantinh-mikroglyptikh/', categoriesView, name='byzantinh_mikroglyptikh'),
    path('categories/diafores-kataskeyes/', categoriesView, name='diafores_kataskeyes'),
]
