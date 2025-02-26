
from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_index, name=''),
    path('detail/<int:pk>/',views.view_detail, name='detail'),
    path('cars_create/', views.cars_create),
    path('car_create_2/', views.car_create_2),
    path('car_detail/<int:pk>/', views.car_detail, name='detail')
]
