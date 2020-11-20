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


def product(request, product_id):
    """Display a list of products according to the user research"""
    product = Product.objects.get(pk=product_id)

    context = {
        "product": product,
    }

    return render(request, "food_choice/product.html", context)


def products(request):
    """Display a list of products according to the user research"""
    if request.method == "POST":
        user_research = request.POST["user_research"]

        products = Product.objects.filter(
            name__icontains=user_research.lower(),
        )

        context = {
            "title": user_research,
            "sentence": "Vous recherchez peut-être...",
            "research": "products",
            "products": products,
        }

        return render(request, "food_choice/research_results.html", context)


def substitutes(request, product_id):
    """Display the detailed sheet of the selected product"""
    product = Product.objects.get(pk=product_id)  # find the product in BD

    categories = Category.objects.filter(
        product__name=product.name
    ).distinct()  # find its categories

    # find similare products wich share at least 4 categories,
    # with the same or a better nutrition grade
    # and order by grade
    substitutes = (
        Product.objects.filter(categories__in=categories)
        .annotate(nb_cat=Count("categories"))
        .filter(nb_cat__gte=4)
        .filter(nutrition_grade__lt=product.nutrition_grade)
        .exclude(nutrition_grade="")
        .order_by("nutrition_grade")
    )

    context = {
        "title": product.name,
        "sentence": "Vous pouvez substituer votre recherche par...",
        "research": "substitutes",
        "products": substitutes,
    }

    return render(request, "food_choice/research_results.html", context)


@login_required
def favorites(request):
    """display the user's favorite products, if he's logged in"""

    # TODO: complete this view

    context = {
        "title": "Mes favoris",
        "research": "favorites",
        "products": products,
    }

    return render(request, "food_choice/research_results.html", context)
