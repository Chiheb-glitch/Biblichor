from django.urls import path
from . import views 

urlpatterns = [
    path('add_book_cart/<slug:code_a_barre>',views.add_cart,name='add_cart'),
   

] 
