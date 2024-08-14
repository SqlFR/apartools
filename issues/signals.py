from django.db.models.signals import post_migrate
from django.dispatch import receiver
from issues.models import Issue


# Ajoute les types d'incidents automatiquement (lors d'une migration)
@receiver(post_migrate)
def add_default_issue(sender, **kwargs):
    if sender.name == 'main':
        default_issue = [
            'Article(s) manquant(s)',
            'Défault de construction',
            'Electricité',
            'Plomberie',
            'Internet',
            'Autres'
        ]

        for issue in default_issue:
            Issue.objects.get_or_create(name=issue)
