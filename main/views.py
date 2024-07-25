from django.shortcuts import render, get_object_or_404
from main.models import Apartment


def index(request):
    apartments = Apartment.objects.all()

    context = {
        'apartments': apartments
    }
    return render(request, 'main/index.html', context)


def detail(request, slug):
    apartment = get_object_or_404(Apartment, slug=slug)
    return render(request, 'main/detail.html', {'apartment': apartment})
