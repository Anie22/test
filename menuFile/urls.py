from django.urls import path
from .views import menu

urlpatterns = [
    path("/download", menu, name="menu"),
]
