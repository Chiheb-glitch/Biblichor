
from django.urls import path
from . import views 

urlpatterns = [
    path('',views.store,name='store'),
    path('category/<slug:category_slug>/',views.store,name='book_by_category'),
    path('add_book/',views.Add_book,name='Add_book'),
    path('category/<slug:category_slug>/<slug:code_a_barre>',views.book_detail,name='book_detail'),
    path('search/',views.search,name='search'),
    path('filter/',views.filter,name='filter'),


] 
