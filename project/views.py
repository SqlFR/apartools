from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from project.models import Apartment


@login_required()
def index(request):
    apartments = Apartment.objects.all()

    context = {
        'apartments': apartments
    }
    return render(request, 'project/index.html', context)


@login_required()
def detail(request, slug):
    apartment = get_object_or_404(Apartment, slug=slug)
    # if request.method == 'POST':
    #     form_add_issue = FormAddIssue(request.POST, apartment=apartment)
    #
    # context = {
    #     'apartment': apartment,
    #     'fr'
    # }
    return render(request, 'project/detail.html', {'apartment': apartment})
