from django.db import models

# Create your models here.


class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    # TODO: Si vous essayez d’enregistrer une instance d’un modèle
    # avec une valeur d’un champ unique dupliquée, une exception
    # django.db.IntegrityError sera levée par la méthode save() du modèle.

    def __str__(self):
        return f"{self.category_name}"


class Product(models.Model):
    product_name = models.CharField(max_length=150, blank=True)
    code = models.PositiveBigIntegerField(default=0)
    brand = models.CharField(max_length=100, blank=True)
    photo_uri = models.TextField(blank=True)
    product_uri = models.TextField(blank=True)
    nutrition_grade = models.CharField(max_length=1)
    energy_100g = models.PositiveSmallIntegerField(default=0)
    fat = models.PositiveSmallIntegerField(default=0)
    saturates = models.PositiveSmallIntegerField(default=0)
    carbohydrate = models.PositiveSmallIntegerField(default=0)
    sugars = models.PositiveSmallIntegerField(default=0)
    protein = models.PositiveSmallIntegerField(default=0)
    fiber = models.PositiveSmallIntegerField(default=0)
    salt = models.PositiveSmallIntegerField(default=0)
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
    date = models.DateTimeField(auto_now_add=True)
