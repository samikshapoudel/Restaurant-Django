from django.urls import path
from . import views

app_name = 'menu'

urlpatterns = [

    path('', views.menu_list, name = 'menu_list'),
    path('<slug:slug>', views.meal_detail, name='meal_detail'),

]
