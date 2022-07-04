from statistics import mode
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=45)
    menu = models.ForeignKey('Menu',on_delete=models.CASCADE)

    class Meta:
        db_table = "categories"


class Menu(models.Model):
    name = models.CharField(max_length=45)

    class Meta:
        db_table = "menus"


class Drink(models.Model):
    korean_name = models.CharField(max_length=45)
    english_name = models.CharField(max_length=45)
    description = models.TextField(null = True)
    category = models.ForeignKey('Category',on_delete=models.CASCADE)

    class Meta:
        db_table = "drinks"


class Allergy_drink(models.Model):
    allergy = models.ForeignKey('allergy',on_delete=models.CASCADE)
    drink = models.ForeignKey('drink',on_delete=models.CASCADE)

    class Meta:
        db_table = "allergy_drinks"


class Nutrition(models.Model):
    one_serving_kca = models.DecimalField(max_digits=10, decimal_places=2)
    sodium_mg = models.DecimalField(max_digits=10, decimal_places=2)
    saturated_fat_g = models.DecimalField(max_digits=10, decimal_places=2)
    sugars_g = models.DecimalField(max_digits=10, decimal_places=2)
    protein_g = models.DecimalField(max_digits=10, decimal_places=2)
    caffeine_mg = models.DecimalField(max_digits=10, decimal_places=2)
    drink = models.ForeignKey('drink',on_delete=models.CASCADE)
    size = models.ForeignKey('size',on_delete=models.CASCADE)

    class Meta:
        db_table = "nutritions"

class Allergy_drink(models.Model):
    allergy = models.ForeignKey('allergy',on_delete=models.CASCADE)
    drink = models.ForeignKey('drink',on_delete=models.CASCADE)

    class Meta:
        db_table = "allergy_drinks"

class Image(models.Model):
    image_url = models.CharField(max_length=2000)
    drink = models.ForeignKey('drink',on_delete=models.CASCADE)

    class Meta:
        db_table = "images"


class Allergy(models.Model):
    name = models.CharField(max_length=45)

    class Meta:
        db_table = "allergies"


class Size(models.Model):
    name = models.CharField(max_length=45)
    size_ml = models.CharField(max_length=45)
    size_fluid_ounce = models.CharField(max_length=45)

    class Meta:
        db_table = "sizes"

# Create your models here.
