from django.urls import path
from .views import menu

urlpatterns = [
    path("menu/download", menu, name="menu"),
]
