from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.text import slugify
from django.db.models.signals import post_save
from django.dispatch import receiver


class CustomMinValueValidator(MinValueValidator):
    def __init__(self, limit_value, message=None):
        super().__init__(limit_value, message=message or f'La valeur doit être au moins de {limit_value}.')


class CustomMaxValueValidator(MaxValueValidator):
    def __init__(self, limit_value, message=None):
        super().__init__(limit_value, message=message or f'La valeur ne peut pas dépasser {limit_value}.')


class Apartment(models.Model):
    name = models.CharField(max_length=32, unique=True, error_messages={
        'unique': 'Un appartement portant ce nom éxiste déjà.'
    }, verbose_name='Nom')
    slug = models.SlugField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)
    bedroom = models.PositiveSmallIntegerField(default=1,
                                               validators=[
                                                    CustomMinValueValidator(1,
                                                                            f'Au moins 1 chambre ! On dort où sinon ?'),

                                                    CustomMaxValueValidator(12)
                                                           ],
                                               verbose_name='Chambre')
    bathroom = models.PositiveSmallIntegerField(default=1,
                                                validators=[
                                                   CustomMaxValueValidator(6)
                                                ],
                                                verbose_name='Salle de bain')
    kitchen = models.PositiveSmallIntegerField(default=1, verbose_name='Cuisine')

    class Meta:
        verbose_name = 'Appartement'
        verbose_name_plural = 'Appartements'

    # Met la première lettre du champ 'name' en majuscule
    def save(self, *args, **kwargs):
        self.name = self.name.capitalize()
        super(Apartment, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


@receiver(post_save, sender=Apartment)
def add_slug_to_apart_when_created(created, instance, **kwargs):
    if created:
        instance.slug = slugify(instance.name)
        instance.save()
