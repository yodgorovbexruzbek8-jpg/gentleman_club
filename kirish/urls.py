from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import *

urlpatterns = [
    path("", register, name="register"),
    path("login/", login, name="login"),
    path("profil/", profil, name="profil"),
    path("logout/", LogoutView.as_view(next_page="login"), name="logout"),
]