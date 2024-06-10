from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseNotFound, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from customers.forms import CustomerModelForm, ContractModelForm, InvoiceModelForm
from customers.models import Customer, Contract, Invoice


#### Customer Views ######
def customer_list(request):
    customers = Customer.objects.all()

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
        "customer": customer,
    }

    return render(request, "customers/customer_detail.html", ctx)


def customer_update(request, pk):
    customer = get_object_or_404(Customer, pk=pk)

    if request.method == "GET":
        form = CustomerModelForm(instance=customer)
        ctx = {
            "form": form,
            "id": pk,
            "customer": customer
        }
        return render(request, "customers/customer_update.html", ctx)

    if request.method == "POST":
        form = CustomerModelForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect("customer_list")

        ctx = {
            "form": form,
            "customer": customer
        }
        return render(request, "customers/customer_update.html", ctx)


def customer_delete(request, pk):
    try:
        customer = Customer.objects.get(pk=pk)
    except Customer.DoesNotExists:
        return redirect("customer_list")

    if request.method == "GET":
        ctx = {
            "customer": customer,
            "id": pk,
        }
        return render(request, "customers/customer_delete.html", ctx)

    if request.method == "POST":
        customer.delete()
        messages.success(request, f"Klient {customer.name} został poprawnie usunięty")
        return redirect("customer_list")

    return HttpResponse("Method not allowed", status_code=405)


@login_required
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
            customer.created_by = request.user
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



#### Contract Views #####


@login_required
def contract_create(request):
    if request.method == "GET":
        form = ContractModelForm()
        ctx = {
            "form": form
        }

        return render(request, "contracts/contract_create.html", ctx)

    if request.method == "POST":
        form = ContractModelForm(request.POST)
        if form.is_valid():
            contract = form.save(commit=False)
            contract.created_by = request.user
            contract.save()
            form.save_m2m()

            ctx = {
                "contract": contract,
                "form": ContractModelForm()
            }
            return render(request, "contracts/contract_create.html", ctx)

        ctx = {
            "form": form
        }
        return render(request, "contracts/contract_create.html", ctx)


def contract_detail(request, pk):
    try:
        contract = Contract.objects.get(pk=pk)
    except ObjectDoesNotExist:
        return HttpResponseNotFound("Contract does not exist")

    ctx = {
        "contract": contract,
    }
    return render(request, "contracts/contract_detail.html", ctx)


def contract_list(request):
    contracts = Contract.objects.all()

    ctx = {
        "contracts": contracts
    }

    return render(request, "contracts/contract_list.html", ctx)


def contract_delete(request, pk):
    try:
        contract = Contract.objects.get(pk=pk)
    except Contract.DoesNotExists:
        return redirect("customer_list")

    if request.method == "GET":
        ctx = {
            "contract": contract,
            "id": pk,
        }
        return render(request, "contracts/contract_delete.html", ctx)

    if request.method == "POST":
        contract.delete()
        messages.success(request, f"Umowa o numerze {contract.number} został poprawnie usunięty")
        return redirect("customer_list")

    return HttpResponse("Method not allowed", status_code=405)



def contract_update(request, pk):
    contract = get_object_or_404(Contract, pk=pk)

    if request.method == "GET":
        form = ContractModelForm(instance=contract)
        ctx = {
            "form": form,
            "id": pk,
            "contract": contract,
        }
        return render(request, "contracts/contract_update.html", ctx)

    if request.method == "POST":
        form = ContractModelForm(request.POST, instance=contract)
        if form.is_valid():
            form.save()
            return redirect("customer_list")

        ctx = {
            "form": form,
            "contract": contract,
        }
        return render(request, "contracts/contract_update.html", ctx)


#### Invoices Views #####

@login_required
def invoice_create(request):
    if request.method == "GET":
        form = InvoiceModelForm()

        ctx = {
            "form": form
        }
        return render(request, "invoices/invoice_create.html", ctx)

    if request.method == "POST":
        form = InvoiceModelForm(request.POST)
        if form.is_valid():
            invoice = form.save(commit=False)
            invoice.created_by = request.user
            invoice.save()

            ctx = {
                "form": InvoiceModelForm(),
                "invoice": invoice,
            }
            return render(request, "invoices/invoice_create.html", ctx)

        ctx = {
            "form": form
        }
        return render(request, "invoices/invoice_create.html", ctx)


def invoice_detail(request, pk):
    try:
        invoice = Invoice.objects.get(pk=pk)
    except ObjectDoesNotExist:
        return HttpResponseNotFound("Invoice does not exist")

    ctx = {
        "invoice": invoice,
    }
    return render(request, "invoices/invoice_detail.html", ctx)


def invoice_list(request):
    invoices = Invoice.objects.all()

    ctx = {
        "invoices": invoices
    }
    return render(request, "invoices/invoice_list.html", ctx)


def invoice_delete(request, pk):
    try:
        invoice = Invoice.objects.get(pk=pk)
    except Invoice.DoesNotExists:
        return redirect("customer_list")

    if request.method == "GET":
        ctx = {
            "invoice": invoice,
            "id": pk,
        }
        return render(request, "invoices/invoice_delete.html", ctx)

    if request.method == "POST":
        invoice.delete()
        messages.success(request, f"Faktura o numerze {invoice.number} został poprawnie usunięty")
        return redirect("customer_list")

    return HttpResponse("Method not allowed", status_code=405)


def invoice_update(request, pk):
    invoice = get_object_or_404(Invoice, pk=pk)

    if request.method == "GET":
        form = InvoiceModelForm(instance=invoice)

        ctx = {
            "form": form,
            "invoice": invoice,
            "id": pk,
        }
        return render(request, "invoices/invoice_update.html", ctx)

    if request.method == "POST":
        form = InvoiceModelForm(request.POST, instance=invoice)
        if form.is_valid():
            form.save()
            return redirect("customer_list")

        ctx = {
            "form": form,
            "invoice": invoice,
        }
        return render(request, "invoices/invoice_update.html", ctx)
