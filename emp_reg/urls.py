from django.urls import path, include, re_path
from django.contrib import admin
from . import views

urlpatterns = [

    
    

    path('', views.emp_home, name='emp_home'),
    # re_path('', views.emp_home, name='emp_home'),
    # path('emp/login', views.LoginView, name ='login'),
    # path('emp/list', views.emp_list, name='emp_list'),
    path('emp/new',views.emp_new, name='emp_new'),
    path('emp/deleted-record',views.emp_del_list, name='emp_del_list'),
    path('emp/<int:pk>/edit', views.emp_edit, name='emp_edit'),
    path('emp/<int:pk>/remove', views.emp_remove, name='emp_remove'),
    path('emp/<int:pk>/delete', views.emp_delete, name='emp_delete'),
    path('emp/<int:pk>/restore', views.emp_restore, name='emp_restore'),
    path('emp/<int:pk>/rest_conf', views.emp_rest_conf, name='emp_rest_conf'),
    path('ajax/load-roles/', views.load_roles, name='ajax_load_roles'),

    path('emp/<str:email>/detail', views.emp_detail, name='emp_detail'), 
    path('emp/<str:email>/emp_user_edit', views.emp_user_edit, name='emp_user_edit'),
    path('emp/update_password', views.update_password, name='update_password'),

    #path('emp/search',views.emp_search, name='emp_search'),
    #path('emp/del_search',views.emp_del_search, name='emp_del_search'),
]