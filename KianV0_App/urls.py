from django.urls import path, include
from . import views

urlpatterns = [
    path('index/', views.view_of__index),
    path('un1/', views.view_of__landing_views_counter_incremnet), #this one will return what nth visitor are your; cosmetic one
]
