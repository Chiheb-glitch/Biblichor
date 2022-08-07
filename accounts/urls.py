from django.contrib import admin
from django.urls import path , include
from . import views 
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
      path('login/', views.login , name='login'),
          path('logout/', views.logout , name='logout'),
          path('activate/<uidb64>/<token>',views.activate,name='activate'),
    path('register/', views.register , name='register'),
      path('register1/', views.register1 , name='register1'),
    path('register2/', views.register2 , name='register2'),

    path('dashboard/',views.dashboard,name='dashboard'),
    path('forgotPassword/',views.forgotPassword,name='forgotPassword'),
    path('resetpassword_validate/<uidb64>/<token>',views.resetpassword_validate,name='resetpassword_validate'),
    path('resetPassword/',views.resetPassword,name='resetPassword'),

      ] 