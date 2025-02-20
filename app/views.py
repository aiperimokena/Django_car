from django.shortcuts import render
from .models import Car, Color, Category

def view_index(request):
    cars = Car.objects.all()

    return render(request, 'app/index.html', {'cars': cars})


def view_detail(request, pk):
    detail = Car.objects.get(id=pk)

    return render(request, 'app/detail.html', {'detail': detail})