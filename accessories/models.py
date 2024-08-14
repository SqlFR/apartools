from django.db import models

from project.models import Apartment


class AccessoryType(models.Model):
    ROOM_CHOICES = (
        ('KITCHEN', 'Cuisine'),
        ('BEDROOMS', 'Chambres'),
        ('BATHROOM', 'Salle de bain'),
        ('COMMON', 'Espaces communs')
    )
    name = models.CharField(max_length=24, unique=True, verbose_name='Nom')
    room = models.CharField(max_length=24, choices=ROOM_CHOICES,
                            default='KITCHEN', verbose_name='Pièce')

    # Met la première lettre du champ 'name' en majuscule
    def save(self, *args, **kwargs):
        self.name = self.name.capitalize()
        super(AccessoryType, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Accessoire'
        verbose_name_plural = 'Accessoires'

    def __str__(self):
        return self.name


class Accessory(models.Model):
    STATUS_CHOICES = [
        ('NOT_HANDLED', 'Non traité'),
        ('NOT_AVAILABLE', 'Indisponible'),
        ('HANDLED', 'Préparé'),
        ('DELIVERY', 'Livré')
    ]

    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE)
    accessory = models.ForeignKey(AccessoryType, on_delete=models.CASCADE)
    status = models.CharField(max_length=24, choices=STATUS_CHOICES, default='NOT_HANDLED')

    def __str__(self):
        return f"{self.accessory.name}"

    class Meta:
        unique_together = ('apartment', 'accessory')  # Chaque paire doit être unique
        verbose_name = 'Accessoire'
        verbose_name_plural = 'Accessoires'
