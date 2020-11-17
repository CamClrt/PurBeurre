from django.urls import path
from . import views


app_name = "food_choice"
urlpatterns = [
    path("", views.home, name="home"),
    path("products/", views.products, name="products"),
    path("favorites/", views.favorites, name="favorites"),
]
