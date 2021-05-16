from django.http import HttpResponse
from .models import Image
from django.shortcuts import render
import numpy as np


def index(request):
    return HttpResponse("Hello, world.")

def show(request):
    all_images = Image.objects.all()
    images = all_images[np.random.randint(0, len(all_images))]
    context = {'images':images}
    return render(request, 'oekaki/show.html', context)