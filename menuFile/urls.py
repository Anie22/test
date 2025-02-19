from django.urls import path
from .views import menu_dload

urlpatterns = [
    path("", menu_dload, name="menu"),
]
