from django.urls import path
from .views import generate_qr

urlpatterns = [
    path('download_qr/', generate_qr, name='download_qr'),
]