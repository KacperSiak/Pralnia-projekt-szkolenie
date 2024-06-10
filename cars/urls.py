from django.urls import path
from cars.views import (
    car_list,
    car_detail,
    car_create,
    car_delete,
    car_update,
)

urlpatterns = [
    path("car_list", car_list, name='car_list'),
    path("car_detail/<int:pk>", car_detail, name='car_detail'),
    path("car_create", car_create, name='car_create'),
    path("car_update/<int:pk>", car_update, name='car_update'),
    path("car_delete/<int:pk>", car_delete, name='car_delete'),
]
