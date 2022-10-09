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
    path('add_review/<str:username>',views.add_review,name='add_review'),
    path('edit_profile/account',views.edit_profile_account,name='edit_profile_account'),
        path('edit_profile/security',views.edit_profile_security,name='edit_profile_security'),
                path('edit_profile/adress',views.edit_profile_adress,name='edit_profile_adress'),
        path('edit_profile/security_pass',views.edit_profile_security_password,name='edit_profile_security_password'),
        path('edit_profile/security_email',views.edit_profile_security_email,name='edit_profile_security_email'),
        path('edit_profile/security_phone',views.edit_profile_security_phone,name='edit_profile_security_phone'),


    path('dashboard/<str:username>',views.dashboard,name='dashboard'),
    path('forgotPassword/',views.forgotPassword,name='forgotPassword'),
    path('resetpassword_validate/<uidb64>/<token>',views.resetpassword_validate,name='resetpassword_validate'),
    path('resetPassword/',views.resetPassword,name='resetPassword'),

      ] 