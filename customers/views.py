from django.contrib import messages

from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseNotFound, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from customers.forms import CustomerModelForm
from customers.models import Customer


def customer_list(request):
    customers = (
        Customer.objects.all()
    )

    ctx = {
        "customers": customers
    }
    return render(request, "customers/customer_list.html", ctx)


def customer_detail(request, pk):
    try:
        customer = Customer.objects.get(pk=pk)
    except ObjectDoesNotExist:
        return HttpResponseNotFound("Customer does not exist")
    ctx = {
        "customer": customer
    }

    return render(request, "customers/customer_detail.html", ctx)


def customer_update(request, pk):
    customer = get_object_or_404(Customer, pk=pk)

    if request.method == "GER":
        form = CustomerModelForm(instance=customer)
        ctx = {
            "form":form,
            "pk":pk
        }
        return render(request, "customers/customer_update.html", ctx)

    if request.method == "POST":
        form = CustomerModelForm(request.POST, instance=customer)
        if form.is_valid():
            updated_customer = form.save()
            ctx = {
                "customer": updated_customer,
                "form": CustomerModelForm(instance=updated_customer),
            }
            return render(request, "customers/customer_update.html", ctx)

        ctx = {
            "form": form,
        }
        return render(request, "customers/customer_update.html", ctx)


def customer_delete(request, pk):
    try:
        customer = Customer.objects.get(pk=pk)
    except Customer.DoesNotExists:
        return redirect("customer_list")

    if request.method == "GET":
        ctx = {
            "customer": customer
        }
        return render(request, "customers/customer_delete.html", ctx)

    if request.method == "POST":
        customer.delete()
        messages.success(f"Klient {customer.name} został poprawnie usunięty")

        return redirect("customer_list")

    return HttpResponse("Method not allowed", status_code=405)


def customer_create(request):
    if request.method == "GET":
        form = CustomerModelForm()
        ctx = {
            "form": form
        }

        return render(request, "customers/customer_create.html", ctx)

    if request.method == "POST":
        form = CustomerModelForm(request.POST)
        if form.is_valid():
            customer = form.save(commit=False)
            customer.added_by = request.user
            customer.save()

            ctx = {
                "customer": customer,
                "form": CustomerModelForm()
            }
            return render(request, "customers/customer_create.html", ctx)

        ctx = {
            "form": form
        }
        return render(request, "customers/customer_create.html", ctx)

