from django.shortcuts import render, redirect
from .models import Car, Color, Category

def view_index(request):
    cars = Car.objects.all()

    return render(request, 'app/index.html', {'cars': cars})


def view_detail(request, pk):
    detail = Car.objects.get(id=pk)

    return render(request, 'app/detail.html', {'detail': detail})

def cars_create(request):
    if request.method == 'POST':
        title = request.POST['title']
        year = request.POST['year']
        engine_capacity = request.POST['engine_capacity']
        color_id = request.POST['color_id']
        category_id = request.POST['category_id']
        image = request.FILES['image']
        milage = request.POST['milage']


        category = Category.objects.get(id=int(category_id))
        color = Color.objects.get(id=int(color_id))

        car = Car(title=title, category_id=int(category_id), year=int(year), engine_capacity=int(engine_capacity),
                  color_id=int(color_id), image=image, milage= int(milage))

        car.save()


    return render(request,'app/cars_create.html' )