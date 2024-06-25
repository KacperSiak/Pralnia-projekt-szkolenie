from django.urls import path

from customers import views as customer_views


urlpatterns = [
    #### CUSTOMERS #####
    path("customer_list", customer_views.customer_list, name="customer_list"),
    path("customer_detail/<int:pk>", customer_views.customer_detail, name="customer_detail"),
    path("customer_create", customer_views.customer_create, name="customer_create"),
    path("customer_update/<int:pk>", customer_views.customer_update, name="customer_update"),
    path("customer_delete'<int:pk>", customer_views.customer_delete, name="customer_delete"),

    #### CONTRACTS ####
    path("contract_create", customer_views.contract_create, name="contract_create"),
    path("contract_detail/<int:pk>", customer_views.contract_detail, name="contract_detail"),
    path("contract_list", customer_views.contract_list, name="contract_list"),
    path("contract_delete/<int:pk>", customer_views.contract_delete, name="contract_delete"),
    path("contract_update/<int:pk>", customer_views.contract_update, name="contract_update"),


    ### INOVICES ###
    path("invoice_create", customer_views.invoice_create, name="invoice_create"),
    path("invoice_detail/<int:pk>", customer_views.invoice_detail, name="invoice_detail"),
    path("invoice_list", customer_views.invoice_list, name="invoice_list"),
    path("invoice_delete/<int:pk>", customer_views.invoice_delete, name="invoice_delete"),
    path("invoice_update/<int:pk>", customer_views.invoice_update, name="invoice_update"),
]

