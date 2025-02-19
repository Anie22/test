from django.shortcuts import render
import os
from django.conf import settings
from django.http import JsonResponse, FileResponse 

# Create your views here.

def menu(request):
    """Automatically download an image from the app's media folder"""

    # Define the image path (stored inside media/images/)
    image_name = "menu2.jpg"  # Replace with your actual image name
    image_path = os.path.join(settings.MEDIA_ROOT, "menu", image_name)

    # Check if file exists
    if os.path.exists(image_path):
        return FileResponse(open(image_path, "rb"), as_attachment=True, filename=image_name)
    else:
        return JsonResponse({"error": "File not found"}, status=404)
