from django.urls import path, include, re_path
from django.contrib import admin
from . import views

urlpatterns = [

    
    

    path('', views.emp_home, name='emp_home'),
    path('emp/new',views.emp_new, name='emp_new'),
    path('emp/deleted-record',views.emp_del_list, name='emp_del_list'),
    path('emp/<int:pk>/edit', views.emp_edit, name='emp_edit'),
    path('emp/<int:pk>/remove', views.emp_remove, name='emp_remove'),
    path('emp/<int:pk>/delete', views.emp_delete, name='emp_delete'),
    path('emp/<int:pk>/restore', views.emp_restore, name='emp_restore'),
    path('emp/<int:pk>/rest_conf', views.emp_rest_conf, name='emp_rest_conf'),
    path('ajax/load-roles/', views.load_roles, name='ajax_load_roles'),
    path('emp/detail', views.emp_detail, name='emp_detail'),
    path('emp/detail', views.admin_detail, name='admin_detail'), 
    path('emp/emp_user_edit', views.emp_user_edit, name='emp_user_edit'),
    path('emp/update_password', views.update_password, name='update_password'),

]