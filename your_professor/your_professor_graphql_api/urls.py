from django.urls import path
from ariadne_django.views import GraphQLView
from . import views
from .schema import schema
# from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('', views.index, name="index"),
    path('graphql/', GraphQLView.as_view(schema=schema), name='graphql'),
]
