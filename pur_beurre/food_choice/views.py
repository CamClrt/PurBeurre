"""Views used by the application."""

from django.shortcuts import render, redirect
from .forms import HomeResearchForm
from .models import Product, Category, Favoris
from users.models import User
from django.db.models import Count
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.contrib import messages


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


def legal_notices(request):
    """Display the legal notices page of the application"""

    return render(
        request,
        "food_choice/legal_notices.html",
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

    favoris = []
    current_user = request.user
    if current_user != "AnonymousUser":
        favoris_obj = Favoris.objects.filter(owner_id=current_user.id)
        for one_favoris in favoris_obj:
            favoris.append(one_favoris.substitute.id)

    context = {
        "title": product.name,
        "product_url": product.photo_url,
        "searched_product": product_id,
        "sentence": "Vous pouvez substituer votre recherche par...",
        "research": "substitutes",
        "products": substitutes,
        "favoris": favoris,
    }

    return render(request, "food_choice/research_results.html", context)


@login_required
def save_as_favoris(request, product_id, substitute_id):
    """save as the user's favorite product, if he's logged in"""
    current_user = request.user
    # insert product, substitute and user
    product = Product.objects.get(pk=product_id)
    substitute = Product.objects.get(pk=substitute_id)
    user = User.objects.get(pk=current_user.id)
    favoris = Favoris(product=product, substitute=substitute, owner=user)

    try:
        favoris.save()
        return redirect("food_choice:favorites")
    except IntegrityError:
        messages.error(
            request,
            f"Erreur: {substitute.name} n'a pas pu être enregistré",
        )
        return redirect("food_choice:home")


@login_required
def favorites(request):
    """display the user's favorite products, if he's logged in"""
    current_user = request.user
    favoris_obj = Favoris.objects.filter(owner_id=current_user.id)

    favoris = []
    for one_favoris in favoris_obj:
        favoris.append(one_favoris.substitute)

    context = {
        "title": "Mes produits favoris",
        "research": "favorites",
        "products": favoris,
    }

    return render(request, "food_choice/research_results.html", context)
