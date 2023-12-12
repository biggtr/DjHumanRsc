from django.shortcuts import render

# Create your views here.


def LandingPageView(request):
    return render(request, "landing_page.html")


def HomePageView(request):
    return render(request, "home.html")
