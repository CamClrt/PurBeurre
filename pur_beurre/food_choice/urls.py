"""Centralize the application urls"""

from django.urls import path
from . import views


app_name = "food_choice"
urlpatterns = [
    path("", views.home, name="home"),
    path("product/<int:product_id>/", views.product, name="product"),
    path("products/", views.products, name="products"),
    path("substitutes/<int:product_id>/", views.substitutes, name="substitutes"),
    path("favorites/", views.favorites, name="favorites"),
]
