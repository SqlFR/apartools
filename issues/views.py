from django.shortcuts import get_object_or_404, redirect, render, reverse
from django_ratelimit.decorators import ratelimit
from django.views.decorators.http import require_http_methods

from main.models import Apartment
from models import Issue
from main.forms import IssueForm, EditIssueForm


@ratelimit(key='user_or_ip', rate='10/ms')
def add_issue(request, apartment_id):
    apartment = get_object_or_404(Apartment, id=apartment_id)
    if request.method == 'POST':
        form = IssueForm(request.POST, apartment=apartment)
        rendered_form = form.render("issues/snippets/form_add_issue_snippet.html")
        if form.is_valid():
            form.instance.apartment = apartment
            form.save()
            return redirect(f"{reverse('main:add_issue', kwargs={'apartment_id': apartment.id})}?success=1")
    else:
        form = IssueForm(apartment=apartment, label_suffix='')
        rendered_form = form.render("issues/snippets/form_add_issue_snippet.html")
    context = {
        'apartment': apartment,
        'form': rendered_form
    }

    return render(request, 'main/add_issue.html', context)


@require_http_methods(['DELETE'])
def delete_issue(request, issue_id, *args):
    issue = get_object_or_404(Issue, id=issue_id)
    issue.delete()
    return redirect('main:results', apartment_id=issue.apartment.id)


@require_http_methods(['EDIT'])
def edit_issue(request, issue_id):
    issue = get_object_or_404(Issue, id=issue_id)
    apartment = get_object_or_404(Apartment, id=issue.apartment.id)

    if request.method == 'POST':
        form = EditIssueForm(request.POST, instance=issue, apartment=apartment)
        if form.is_valid():
            form.save()
            return redirect('main:results', apartment_id=apartment.id)
    else:
        form = EditIssueForm(instance=issue, apartment=apartment, issue_choice_user=issue.issue)

    context = {
        'form': form,
        'issue': issue,
        'apartment': apartment
    }

    return render(request, 'main/edit_issue.html', context)

