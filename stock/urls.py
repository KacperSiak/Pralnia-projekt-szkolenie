from django.urls import path

from stock.views import stock_list, stock_detail, stock_create, stock_update, stock_delete

urlpatterns = [
    path("stock_list", stock_list, name="stock_list"),
    path("stock_detail/<int:pk>", stock_detail, name="stock_detail"),
    path("stock_create", stock_create, name="stock_create"),
    path("stock_update/<int:pk>", stock_update, name="stock_update"),
    path("stock_delete'<int:pk>", stock_delete, name="stock_delete"),
]
