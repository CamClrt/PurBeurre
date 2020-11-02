from django.shortcuts import render


def home_page(request):
    return render(request, "food_choice/home.html")

