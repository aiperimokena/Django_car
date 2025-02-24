
from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_index),
    path('detail/<int:pk>/',views.view_detail, name='detail'),
    path('cars_create/', views.cars_create)
]
