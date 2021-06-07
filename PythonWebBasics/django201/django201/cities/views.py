from django.http import HttpResponse
from django.shortcuts import render
from django.template.context_processors import request

from django201.cities.models import Person


def index(req):
    context = {
        'name': 'Stefan Dimitrov',
        'people': Person.objects.all()

    }

    return render(req, 'index.html', context)


def list_phones(request):
    context = {
        'phones': [
            {
                'name':'Galaxy 5000',
                'quantity': 3,
            },
            {
                'name': 'Xiaomi Readmi T9',
                'quantity': 5,
            },
            {
                'name': 'iPhone 12',
                'quantity': 2,
            },

        ]
    }
    return render(request, 'phones.html', context)