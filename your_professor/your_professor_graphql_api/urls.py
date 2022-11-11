from django.urls import path
from ariadne_django.views import GraphQLView
from django.views.decorators.clickjacking import xframe_options_exempt

from . import views
from .schema import schema

urlpatterns = [
    path('', views.index, name="index"),
    path('graphql/', GraphQLView.as_view(schema=schema), name='graphql'),
]

