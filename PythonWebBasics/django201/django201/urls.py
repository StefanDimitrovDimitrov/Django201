
from django.contrib import admin
from django.urls import path, include

from django201.cities.views import index, list_phones


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('django201.cities.urls')),
    path('', include('django201.people.urls'))
]
