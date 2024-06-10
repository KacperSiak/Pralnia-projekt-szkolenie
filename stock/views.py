from django.shortcuts import render, get_object_or_404, redirect

from .models import Stock
from .forms import StockForm


def stock_list(request):
    stocks = Stock.objects.all()
    return render(request, "stock/stock_list.html", {"stocks": stocks})


def stock_detail(request, pk):
    stock = get_object_or_404(Stock, pk=pk)
    return render(request, "stock/stock_detail.html", {"stock": stock})


def stock_create(request):
    if request.method == "POST":
        form = StockForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("stock_list")
    else:
        form = StockForm()
    return render(request, "stock/stock_create.html", {"form": form})


def stock_update(request, pk):
    stock = get_object_or_404(Stock, pk=pk)
    if request.method == "POST":
        form = StockForm(request.POST, instance=stock)
        if form.is_valid():
            form.save()
            return redirect("stock_list")
    else:
        form = StockForm(instance=stock)
    return render(request, "stock/stock_update.html", {"form": form, "stock": stock})


def stock_delete(request, pk):
    stock = get_object_or_404(Stock, pk=pk)
    if request.method == "POST":
        stock.delete()
        return redirect("stock_list")
    return render(request, "stock/stock_delete.html", {"stock": stock})



