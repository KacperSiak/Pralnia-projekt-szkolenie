from django.shortcuts import render, get_object_or_404, redirect
from .models import Cars
from .forms import CarsForm

def car_list(request):
    cars = Cars.objects.all()
    return render(request, 'cars/car_list.html', {'cars': cars})

def car_detail(request, pk):
    car = get_object_or_404(Cars, pk=pk)
    return render(request, 'cars/car_detail.html', {'car': car})

def car_create(request):
    if request.method == 'POST':
        form = CarsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('car_list')
    else:
        form = CarsForm()
    return render(request, 'cars/car_form.html', {'form': form})

def car_update(request, pk):
    car = get_object_or_404(Cars, pk=pk)
    if request.method == 'POST':
        form = CarsForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('car_list')
    else:
        form = CarsForm(instance=car)
    return render(request, 'cars/car_form.html', {'form': form})

def car_delete(request, pk):
    car = get_object_or_404(Cars, pk=pk)
    if request.method == 'POST':
        car.delete()
        return redirect('car_list')
    return render(request, 'cars/car_delete.html', {'car': car})

