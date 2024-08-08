from django.shortcuts import get_object_or_404, redirect, render, reverse
from django_ratelimit.decorators import ratelimit
from django.views.decorators.http import require_http_methods

from project.models import Apartment
from issues.models import Issue
from issues.forms import FormAddIssue


@ratelimit(key='user_or_ip', rate='10/ms')
def add_issue(request, slug):
    apartment = get_object_or_404(Apartment, slug=slug)
    if request.method == 'POST':
        form_add_issue = FormAddIssue(request.POST, apartment=apartment)
        if form_add_issue.is_valid():
            form_add_issue.instance.apartment = apartment
            form_add_issue.save()
            return redirect(f"{reverse('issues:add_issue', kwargs={'slug': apartment.slug})}?success=1")
    else:
        form_add_issue = FormAddIssue(apartment=apartment, label_suffix='')
    context = {
        'apartment': apartment,
        'form_add_issue': form_add_issue
    }

    return render(request, 'issues/add_issue.html', context)


@require_http_methods(['DELETE'])
def delete_issue(request, issue_id, *args):
    issue = get_object_or_404(Issue, id=issue_id)
    print('L\'issue dans la fonction delete_issue', issue)
    issue.delete()
    return redirect('project:details', apartment_id=issue.apartment.id)


# @require_http_methods(['EDIT'])
# def edit_issue(request, issue_id):
#     issue = get_object_or_404(Issue, id=issue_id)
#     apartment = get_object_or_404(Apartment, id=issue.apartment.id)
#
#     if request.method == 'POST':
#         form = EditIssueForm(request.POST, instance=issue, apartment=apartment)
#         if form.is_valid():
#             form.save()
#             return redirect('project:results', apartment_id=apartment.id)
#     else:
#         form = EditIssueForm(instance=issue, apartment=apartment, issue_choice_user=issue.issue)
#
#     context = {
#         'form': form,
#         'issue': issue,
#         'apartment': apartment
#     }
#
#     return render(request, 'project/edit_issue.html', context)

