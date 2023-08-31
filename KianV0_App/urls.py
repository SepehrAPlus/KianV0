from django.urls import path, include
from . import views

urlpatterns = [
    path("IntroLandingPage/", views.view__IntroLandingPage),
    path("MainPage/", views.view__MainPage)
]
