from django.urls import path
from . import views

app_name = 'reservation'

urlpatterns = [

    path('reserve_table/', views.reserve_table, name = 'reserve_table'),


]
