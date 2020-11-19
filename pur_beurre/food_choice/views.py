"""Views used by the application."""

from django.shortcuts import render
from .forms import HomeResearchForm
from .models import Product, Category
from django.db.models import Count
from django.contrib.auth.decorators import login_required


def home(request):
    """Display the home page of the application"""

    context = {
        "home_form": HomeResearchForm(),
    }

    return render(
        request,
        "food_choice/home.html",
        context,
    )


def products(request):
    """Display a list of products according to the user research"""
    if request.method == "POST":
        user_research = request.POST["user_research"]

        products = Product.objects.filter(
            name__icontains=user_research.lower(),
        )

        context = {
            "user_research": user_research,
            "products": products,
        }

        return render(request, "food_choice/products.html", context)


def product(request, product_id):
    """Display a list of products according to the user research"""
    product = Product.objects.get(pk=product_id)
    categories = Category.objects.filter(product__name=product.name).distinct()

    context = {
        "product": product,
        "categories": categories,
    }

    return render(request, "food_choice/product.html", context)


def substitutes(request, product_id):
    """Display the detailed sheet of the selected product"""
    product = Product.objects.get(pk=product_id)  # find the product in BD

    categories = Category.objects.filter(
        product__name=product.name
    ).distinct()  # find its categories

    # find similare products wich share at least 4 categories,
    # with the same or a better nutrition grade
    # and order by this grade
    substitutes = (
        Product.objects.filter(categories__in=categories)
        .distinct()
        .annotate(nb_cat=Count("categories"))
        .filter(nb_cat__gte=4)
        .filter(nutrition_grade__lt=product.nutrition_grade)
        .exclude(nutrition_grade="")
        .order_by("nutrition_grade")
    )

    context = {
        "product": product,
        "substitutes": substitutes,
    }

    return render(request, "food_choice/substitutes.html", context)


@login_required
def favorites(request):
    """display the user's favorite products, if he's logged in"""

    context = {
        "favorites": "",
    }

    return render(request, "food_choice/favorites.html", context)
