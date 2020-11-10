from django.db import models

# from django.contrib.auth.models import User


class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"{self.category_name}"


class Product(models.Model):
    product_name = models.CharField(max_length=150, null=True)
    code = models.CharField(max_length=13, default=(13 * "0"))
    brand = models.CharField(max_length=100, null=True)
    photo_url = models.TextField(null=True)
    product_url = models.TextField(null=True)
    nutrition_grade = models.CharField(max_length=1, null=True)
    energy_100g = models.IntegerField(default=0)
    fat = models.IntegerField(default=0)
    saturates = models.IntegerField(default=0)
    carbohydrate = models.IntegerField(default=0)
    sugars = models.IntegerField(default=0)
    protein = models.IntegerField(default=0)
    fiber = models.IntegerField(default=0)
    salt = models.IntegerField(default=0)
    categories = models.ManyToManyField(Category, related_name="product")

    def __str__(self):
        return (
            f"{self.product_name}, {self.brand}, {self.code}, "
            f"{self.nutrition_grade}, {self.energy_100g}"
        )


class Favoris(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="product"
    )
    product_substitute = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="substitute"
    )
    # user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
