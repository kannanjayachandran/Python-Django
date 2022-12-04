from django.shortcuts import render


def myView(request):
    return render(request, "index.html")