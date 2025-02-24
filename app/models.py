from django.db import models
from django.db.models import PROTECT


class Color(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Color"
        verbose_name_plural = "Colors"


class Category(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Car(models.Model):
    title = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    color = models.ForeignKey(Color, on_delete=models.PROTECT)
    year = models.PositiveIntegerField()
    milage = models.PositiveIntegerField()
    engine_capacity = models.DecimalField(max_digits=3, decimal_places=2)
    image = models.ImageField(upload_to='media/detail_image')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Car"
        verbose_name_plural = "Cars"

