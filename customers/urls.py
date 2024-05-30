from django.urls import path
from django.contrib.auth import views as auth_views

from customers.views import (
    customer_list,
    customer_detail,
    customer_create,
    customer_update,
    customer_delete,
    contract_create,
)


urlpatterns = [
    #### CUSTOMERS #####
    path("customer_list", customer_list, name="customer_list"),
    path("customer_detail/<int:pk>", customer_detail, name="customer_detail"),
    path("customer_create", customer_create, name="customer_create"),
    path("customer_update/<int:pk>", customer_update, name="customer_update"),
    path("customer_delete'<int:pk>", customer_delete, name="customer_delete"),

    #### CONTRACTS ####
    path("contract_create", contract_create, name="contract_create"),
]

