from django.db import models

# Create your models here.
class Serveur(models.Model):
    #Definition des choix pour le statut
    STATUT_CHOICES = [
        ('EN_LIGNE', 'En Ligne'),
        ('HORS_LIGNE', 'Hors Ligne'),
        ('MAINTENANCE', 'En Maintenance')
    ]

    nom = models.CharField(max_length=100)
    adresse_ip = models.GenericIPAddressField()
    statut = models.CharField(max_length=20, choices= STATUT_CHOICES, default='EN_LIGNE')
    ram_utilisee = models.IntegerField(help_text="RAM utilisee en Go")

    def __str__(self):
        return f"{self.nom} ({self.adresse_ip})"