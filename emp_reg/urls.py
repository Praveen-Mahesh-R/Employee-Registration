from django.urls import path
from . import views

urlpatterns = [
    path('', views.emp_list, name='emp_list'),
    path('emp/new',views.emp_new, name='emp_new'),
]