from django.db.models.signals import post_save
from django.dispatch import receiver
from project.models import Apartment
from accessories.models import AccessoryType, Accessory


# Ajoute automatiquement les accessoires (enregistré en db) à la création de l'appart
@receiver(post_save, sender=Apartment)
def add_accessories_when_apartment_created(created, instance, **kwargs):
    if created:
        accessories = AccessoryType.objects.all()

        for accessory in accessories:
            Accessory.objects.create(
                apartment=instance,
                accessory=accessory
            )


# Ajoute l'accessoire qui vient d'être créé à tous les appartements déjà créé
@receiver(post_save, sender=AccessoryType)
def add_accessory_to_apartment_when_created(sender, created, instance, **kwargs):
    if created:
        apartments = Apartment.objects.all()
        for apartment in apartments:
            Accessory.objects.create(
                apartment=apartment,
                accessory=instance
            )
