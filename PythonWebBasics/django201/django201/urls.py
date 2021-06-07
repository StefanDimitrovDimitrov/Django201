
from django.contrib import admin
from django.urls import path

from django201.cities.views import index, list_phones

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('phones/', list_phones),
]
