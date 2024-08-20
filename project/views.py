from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.template.loader import render_to_string
from django_ratelimit.decorators import ratelimit

from accessories.views import accessories_display
from issues.models import Issue
from project.forms import FormAddApart
from project.models import Apartment
from collections import defaultdict


@login_required()
def index(request):
    return render(request, 'project/index.html')


@login_required()
def apartments(request):
    apartments = Apartment.objects.all()

    context = {
        'apartments': apartments,
    }
    return render(request, 'project/apartments.html', context)


@ratelimit(key='user_or_ip', rate='1/s')
def add_apart(request):

    if request.method == 'POST':
        form_add_apart = FormAddApart(request.POST, label_suffix='')

        if form_add_apart.is_valid():

            form_add_apart.save()
            response = HttpResponse(status=200)
            response['HX-Redirect'] = ''
            return response

    else:
        form_add_apart = FormAddApart(label_suffix='')
    context = {
        'form_add_apart': form_add_apart
    }

    return render(request, 'project/add_apart.html', context)


@login_required()
# Vue permettant de voir les détails pour l'appartement sélectionné
def details(request, slug):
    apartment = get_object_or_404(Apartment, slug=slug)
    apartment_issues = Issue.objects.filter(apartment_id=apartment.id)
    apartment_accessories = accessories_display(request, apartment)

    # Initialisation du dictionnaire pour les incidents
    apartment_issues_dict = defaultdict(lambda: defaultdict(list))
    # Ajoute incidents présent dans le dict
    for issue in apartment_issues:
        room = issue.room
        issue_type = issue.issue
        details = issue.details

        apartment_issues_dict[room][issue_type].append((details, issue.id))
    # Conversion en dict normal
    apartment_issues_dict = {room: dict(issues) for room, issues in apartment_issues_dict.items()}

    context = {
        'apartment': apartment,
        'apartment_issues_dict': apartment_issues_dict,
        'apartment_accessories': apartment_accessories,
    }
    return render(request, 'project/details.html', context)
