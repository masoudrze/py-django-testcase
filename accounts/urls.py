from django.urls import path
from .views import login
from .views import logout


urlpatterns = [
    path("login/",login),
    path("logout/",logout),
]