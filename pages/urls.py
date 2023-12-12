from django.urls import path
from . import views

urlpatterns = [
    path("", views.LandingPageView, name="landing-page"),
    path("humanrsc/", views.HomePageView, name="hr-home"),
]
