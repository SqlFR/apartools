from enum import Enum, auto

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.text import slugify
from django.db.models.signals import post_save
from django.dispatch import receiver


class Apartment(models.Model):
    name = models.CharField(max_length=32, unique=True, error_messages={
        'unique': 'Un appartement portant ce nom éxiste déjà.'
    }, verbose_name='Nom')
    slug = models.SlugField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)
    bedroom = models.PositiveSmallIntegerField(default=1,
                                                          validators=[MinValueValidator(1), MaxValueValidator(10)],
                                                          verbose_name='Nombre de chambre')
    bathroom = models.PositiveSmallIntegerField(default=1,
                                                           validators=[MinValueValidator(0), MaxValueValidator(2)],
                                                           verbose_name='Nombre de SDB')

    class Meta:
        verbose_name = 'Appartement'
        verbose_name_plural = 'Appartements'

    # Met la première lettre du champ 'name' en majuscule
    def save(self, *args, **kwargs):
        self.name = self.name.capitalize()
        super(Apartment, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Room(models.Model):
    ROOM_TYPES = [
        ('BE', 'Chambre'),
        ('BA', 'Salle de bain'),
        ('KI', 'Cuisine'),
        ('LI', 'Salon'),
        ('LA', 'Buanderie'),
        ('EN', 'Entrée')
    ]

    name = models.CharField(max_length=128)
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE)
    room_type = models.CharField(max_length=2, choices=ROOM_TYPES)

    def __str__(self):
        return self.name


@receiver(post_save, sender=Apartment)
def add_rooms_for_apartment(sender, instance, created, **kwargs):
    if created:
        # Créer les chambres
        for i in range(instance.bedroom):
            Room.objects.create(name=f"Chambre {i+1}", apartment=instance, room_type='BE')

        # Créer les salles de bain
        for i in range(instance.bathroom):
            Room.objects.create(name=f"Salle de bain {i + 1}", apartment=instance, room_type='BE')

        Room.objects.create(name='Entrée', apartment=instance, room_type='EN')
        Room.objects.create(name='Buanderie', apartment=instance, room_type='LA')
        Room.objects.create(name='Salon', apartment=instance, room_type='LI')
        Room.objects.create(name='Cuisine', apartment=instance, room_type='KI')


@receiver(post_save, sender=Apartment)
def add_slug_to_apart(sender, created, instance, **kwargs):
    if created:
        instance.slug = slugify(instance.name)
        instance.save()
