from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from issues.models import Issue
from project.models import Apartment
from collections import defaultdict


@login_required()
def index(request):
    return render(request, 'project/index.html')


@login_required()
def apartments_list(request):
    apartments = Apartment.objects.all()

    context = {
        'apartments': apartments
    }
    return render(request, 'project/apartments_list.html', context)


@login_required()
# Vue permettant de voir les détails pour l'appartement sélectionné
def details(request, slug):
    apartment = get_object_or_404(Apartment, slug=slug)
    apartment_issues = Issue.objects.filter(apartment_id=apartment.id)

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
    }
    return render(request, 'project/details.html', context)
