from django.shortcuts import render
from django.conf import settings
from django.http import JsonResponse, FileResponse
import qrcode
import os
# import io

# Create your views here.

def generate_qr(request):
    # Get the current request's domain dynamically
    current_host = request.build_absolute_uri("/")[:-1]  # Removes trailing slash
    endpoint = "/menu/download"  # Replace with your actual endpoint
    full_url = f"{current_host}{endpoint}"  # Generates dynamic URL

    # Generate QR Code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(full_url)
    qr.make(fit=True)

    img = qr.make_image(fill="black", back_color="white")

    # Save image to a static folder (media/qr_codes/)
    qr_dir = os.path.join(settings.MEDIA_ROOT, "qr_codes")
    os.makedirs(qr_dir, exist_ok=True)
    qr_path = os.path.join(qr_dir, "qrcode.png")
    img.save(qr_path)

    # Automatically return the file response
    return FileResponse(open(qr_path, "rb"), as_attachment=True, filename="qrcode.png")