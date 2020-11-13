from django.shortcuts import render


def home(request):
    return render(request, "food_choice/home.html")


def results(request):
    if request.method == "POST":
        return render(
            request,
            "food_choice/results.html",
        )
