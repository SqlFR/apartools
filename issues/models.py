from django.db import models

from main.models import Apartment, Room


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
        verbose_name_plural = 'Incident'

    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE, related_name='apartments')
    room = models.ManyToManyField(Room, related_name='apartments')
    issue = models.TextField(verbose_name='Type d\'incident')
    details = models.TextField(verbose_name='Informations complémentaires')
