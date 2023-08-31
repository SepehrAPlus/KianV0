from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def view_of__index(request):
	return HttpResponse("hello :)")


def view_of__landing_views_counter_incremnet(request):
	pass

def view_of__search_shipitems_by(request):
	"""
	A post one 
	"""
