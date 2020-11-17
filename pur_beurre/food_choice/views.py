from django.shortcuts import render
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

        products = Product.objects.all()
        print(products)

        context = {
            "user_research": user_research,
        }

        return render(
            request,
            "food_choice/products.html",
            context,
        )


def favorites(request):
    return render(
        request,
        "food_choice/favorites.html",
    )
