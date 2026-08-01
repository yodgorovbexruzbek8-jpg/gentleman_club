from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path("index/", index, name="index"),
    path("tarix/", tarix, name="tarix"),
    path("profil/", profil, name="profil"),
    path("barberlar/", barberlar, name="barberlar"),
    path("category/barberlar/", views.barberlar, name="barberlar"),
    path("bron/<int:id>/", views.bron, name="bron"),
    path("bronlarim/", views.bronlarim, name="bronlarim"),
]