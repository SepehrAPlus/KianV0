from django.shortcuts import render
from django.http import HttpResponse
from .models import *


def view__IntroLandingPage(request):
	return render(request, r"IntroLandingPage.html")

def view__MainPage(request):
	return render(request, r"MainPage.html")



