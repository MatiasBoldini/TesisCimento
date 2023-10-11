from django.shortcuts import render


def home(request):
    context = {}
    return render(request, "tesisApp/home.html", context)