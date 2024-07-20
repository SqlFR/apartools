from django.db import models

from main.models import Apartment


class TypeIssue(models.Model):
    name = models.CharField(max_length=128, unique=True, verbose_name='Nom')

    class Meta:
        verbose_name = 'Type d\'incident'
        verbose_name_plural = 'Types d\'incidents'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name = self.name.capitalize()
        super(TypeIssue, self).save(*args, **kwargs)


class Issue(models.Model):

    class Meta:
        verbose_name = 'Incident'
        verbose_name_plural = 'Incidents'

    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE)
    # room = models.Ch(choice=create_list_rooms(), verbose_name='pièce')
    issue = models.TextField(verbose_name='Type d\'incident')
    details = models.TextField(verbose_name='Informations complémentaires')



# Crée la liste rooms contenant des tuples de pièce
# def create_list_rooms(apartment: Apartment) -> list[tuple[str, str]]:
#     rooms = [('Entrée', 'Entrée'), ('Cuisine', 'Cuisine'), ('Salon', 'Salon')]
#     rooms += [(f'Chambre {i}', f'Chambre {i}') for i in range(1, apartment.bedroom + 1)]
#     rooms += [(f'Salle de bain {i}', f'Salle de bain {i}') for i in range(1, apartment.bathroom + 1)]
#     rooms += [('Buanderie', 'Buanderie')]

    # return rooms