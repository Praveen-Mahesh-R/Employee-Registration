from django.urls import path

from . import views


urlpatterns = [
    path('login/', views.LoginView, name ='login'),
    path('logout_confirm/', views.logout_check, name ='logout_check'),  
 ]