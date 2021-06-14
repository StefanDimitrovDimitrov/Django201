
from django.contrib import admin
from django.urls import path

from django201.cities.views import index, list_phones, show_forms_demo

urlpatterns = [
    path('', index),
    path('phones/', list_phones),
    path('forms/', show_forms_demo),
]
