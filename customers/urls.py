from django.urls import path
from django.contrib.auth import views as auth_views

from customers.views import (
    customer_list,
    customer_detail,
    customer_create,
    customer_update,
    customer_delete,
    contract_create,
    contract_detail,
    contract_update,
    contract_delete,
    contract_list,
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
    path("contract_detail/<int:pk>", contract_detail, name="contract_detail"),
    path("contract_list", contract_list, name="contract_list"),
    path("contract_delete/<int:pk>", contract_delete, name="contract_delete"),
    path("contract_update/<int:pk>", contract_update, name="contract_update"),
]

