from django.urls import path
from .views import menu_dload

urlpatterns = [
    path("menu/download", menu_dload, name="menu"),
]
