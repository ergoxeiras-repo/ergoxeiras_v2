from django.urls import path
from .views import indexView, categoriesView

urlpatterns = [
    path('', indexView, name='index'),
    path('categories/xyloglypth-forhth-eikona/', categoriesView, name='xyloglypth_forhth_eikona'),
    path('categories/xuloglupth-korniza/', categoriesView, name='xuloglupth_korniza'),
    path('categories/proetoimasia-eikonas/', categoriesView, name='proetoimasia_eikonas'),
    path('categories/kytia-leipsanothikes/', categoriesView, name='kytia_leipsanothikes'),
    path('categories/stauroi/', categoriesView, name='stauroi'),
    path('categories/triptyxa/', categoriesView, name='triptyxa'),
    path('categories/byzantina-mikroglypta/', categoriesView, name='byzantina-mikroglypta'),
    path('categories/diafores-kataskeyes/', categoriesView, name='diafores_kataskeyes'),
    path('categories/erga-pelatwn/', categoriesView, name='erga-pelatwn'),
]
