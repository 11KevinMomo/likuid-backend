import graphene
from graphene_django import DjangoObjectType
from .models import Serveur

# 1. Definir le Type GraphSQL
class ServeurType(DjangoObjectType):
    class Meta: 
        model = Serveur
        fields= ("id", "nom", "adresse_ip", "statut","ram_utilisee")

# 2. Definir la Mutation (modifier le statu)
class UpdateServeurStatus(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        nouveau_statut = graphene.String(required= True)

    serveur = graphene.Field(ServeurType)

    @classmethod
    def mutate(cls, root,info, id, nouveau_statut):
        serveur = Serveur.objects.get(pk=id)
        serveur.statut= nouveau_statut
        serveur.save()
        return UpdateServeurStatus(serveur=serveur)

# 3. Definir les Requetes (Lire les donnees)
class Query(graphene.ObjectType):
    tous_les_serveurs = graphene.List(ServeurType)
    serveurs_hors_ligne = graphene.List(ServeurType)

    def resolve_tous_les_serveurs(root, info):
        return Serveur.objects.all()

    def resolve_serveurs_hors_ligne(root,info):
        return Serveur.objects.filter(statut="HORS_LIGNE")

# 4. Regrouper les Mutations
class Mutation(graphene.ObjectType):
    update_serveur_status = UpdateServeurStatus.Field()

# 5. Creer le schema final
schema = graphene.Schema(query=Query, mutation= Mutation)