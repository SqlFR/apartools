from django.utils.translation import gettext_lazy as _

from django import forms
from django.core.exceptions import ValidationError

from issues.models import Issue, IssueType
from project.models import Room


class FormAddIssue(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ['room', 'issue', 'details']
        widgets = {
            'details': forms.Textarea(attrs={'class': 'form-text-area', 'rows': '2'})
        }

    def clean_details(self):
        details = self.cleaned_data['details']
        return details.capitalize()

    # Récupère l'instance d'appartement
    def __init__(self, *args, **kwargs):
        apartment = kwargs.pop('apartment', None)
        super(FormAddIssue, self).__init__(*args, **kwargs)

        # Récupère les pièces de l'appartement
        rooms = Room.objects.filter(apartment_id=apartment.id)

        if apartment:
            self.fields['room'] = forms.ModelChoiceField(queryset=rooms, initial='', label='Pièce')
            self.fields['issue'] = forms.ModelChoiceField(queryset=IssueType.objects.all(), label='Type d\'incident', initial='')