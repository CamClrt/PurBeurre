from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import HomeResearchForm
from .models import Product


def home(request):
    context = {
        "home_form": HomeResearchForm(),
    }

    return render(
        request,
        "food_choice/home.html",
        context,
    )


def products(request):
    if request.method == "POST":
        user_research = request.POST["user_research"]

        products = Product.objects.filter(
            product_name__icontains=user_research.lower(),
        )

        context = {
            "user_research": user_research,
            "products": products,
        }

        return render(request, "food_choice/products.html", context)


def product(request, product_id):
    product = Product.objects.get(pk=product_id)

    context = {
        "product": product,
    }

    return render(request, "food_choice/product.html", context)


def substitutes(request, product_id):
    product = Product.objects.get(pk=product_id)

    context = {
        "product": product,
    }

    return render(request, "food_choice/substitutes.html", context)


def favorites(request):
    return render(request, "food_choice/favorites.html")
