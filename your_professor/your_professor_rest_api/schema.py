import graphene
from graphene_django import DjangoObjectType
from .models import *


class CountryType(DjangoObjectType):
    class Meta:
        model = Country
        fields = ("local_language_name", "ISO_code_name", "is_active")


# class RegionType(DjangoObjectType):
#     class Meta:
#         model = Region
#         fields = ("local_language_name", "name", "is_active", "country")


class Query(graphene.ObjectType):
    all_countries = graphene.List(CountryType)
    # region_by_name = graphene.Field(RegionType, name=graphene.String(required=True))

    def resolve_all_countries(root, info):
        return Country.objects.select_related("Region").all()

    # def resolve_region_by_name(root, info, name):
    #     try:
    #         return Region.objects.get(name=name)
    #     except Region.DoesNotExist:
    #         return None


schema = graphene.Schema(query=Query)
