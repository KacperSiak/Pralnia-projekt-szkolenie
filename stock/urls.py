from django.urls import path

from stock import views as stock_views

urlpatterns = [
    path("stock_list", stock_views.stock_list, name="stock_list"),
    path("stock_detail/<int:pk>", stock_views.stock_detail, name="stock_detail"),
    path("stock_create", stock_views.stock_create, name="stock_create"),
    path("stock_update/<int:pk>", stock_views.stock_update, name="stock_update"),
    path("stock_delete'<int:pk>", stock_views.stock_delete, name="stock_delete"),
]
