
from django.urls import path
from . import views 

urlpatterns = [
    path('',views.store,name='store'),
    path('add_book/',views.Add_book,name='Add_book'),



] 
