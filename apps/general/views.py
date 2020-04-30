from django.shortcuts import render


def Home(request):
    return render(request, 'general/home.html')


def About(request):
    return render(request, 'general/about.html')