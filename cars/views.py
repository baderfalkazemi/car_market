from django.shortcuts import render, redirect
from .models import Car
from .forms import CarForm

def car_list(request):
    cars = Car.objects.all()
    context = {
        "cars": cars,
    }
    return render(request, 'car_list.html', context)


def car_detail(request, car_id):
    car = Car.objects.get(id=car_id)
    context = {
        "car": car,
    }
    return render(request, 'car_detail.html', context)


def car_create(request):
    form = CarForm()
    if request.method == "POST":
        form = CarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("car-list")
    context = {
        "form":form,
    }
    return render(request, 'create_page.html', context)


def car_update(request, car_id):
    obj = Car.objects.get(id=car_id)
    form = CarForm(instance=obj)
    if request.method == "POST":
        form = CarForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect("car-list")
    context = {
        "obj":obj,
        "form":form,
    }
    return render(request, 'update_page.html', context)

def car_delete(request, car_id):
    Car.objects.get(id=car_id).delete()
    return redirect("car-list")
