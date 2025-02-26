from django.shortcuts import render, redirect
from .models import Car, Color, Category
from .forms import CarCreateForm

def view_index(request):
    cars = Car.objects.all()

    if 'search' in request.GET:
        search = request.GET['search']
        cars = Car.objects.filter(title__icontains=search)


    return render(request, 'app/index.html', {'cars': cars})


def view_detail(request, pk):
    detail = Car.objects.get(id=pk)

    return render(request, 'app/detail.html', {'detail': detail})

def cars_create(request):
    categories = Category.objects.all()
    colors = Color.objects.all()

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

        return redirect ('')

    return render(request, 'app/cars_create.html', {'categories': categories, "colors": colors})

def car_create_2(request):

    if request.method == 'POST':
        form = CarCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("")
    form = CarCreateForm()

    return render(request, 'app/car_create_2.html',{'form': form})

def car_detail(request, pk):

    categories = Category.objects.all()
    colors = Color.objects.all()
    car = Car.objects.get(id=pk)

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

        car.title = title
        car.year = year
        car.engine_capacity = engine_capacity
        car.color_id = color_id
        car.category_id = category_id
        car.milage = milage
        car.image = image

        car.save()
        return redirect('')


    return render(request, 'app/car_detail.html', {'car': car, 'categories': categories, 'colors': colors })