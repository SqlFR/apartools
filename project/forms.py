from django import forms

from project.models import Apartment


class FormAddApart(forms.ModelForm):
    class Meta:
        model = Apartment
        fields = ['name', 'bedroom', 'bathroom']
        labels = {
            'name': "Nom de l'appartement",
            'bedroom': 'Nombre de chambre',
            'bathroom': 'Nombre de SDB'
        }

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control-input'}),
            'bedroom': forms.NumberInput(attrs={'class': 'form-control-input number-input'}),
            'bathroom': forms.NumberInput(attrs={'class': 'form-control-input number-input'}),
        }

    def clean_name(self):
        name = self.cleaned_data.get('name', '')
        return name.strip().capitalize()  # Nettoyer et capitaliser le nom


