from django.http import HttpResponse
from django.core.files.storage import default_storage
from .models import Image
from django.shortcuts import render
import numpy as np
import os
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy


def index(request):
    return HttpResponse("Hello, world.")

def show(request):
    all_images = Image.objects.all()
    images = all_images[np.random.randint(0, len(all_images))]
    context = {'images':images}
    return render(request, 'oekaki/show.html', context)

class DelImage(DeleteView):
    template_name = 'oekaki/image_confirm_delete.html'
    model = Image

    success_url = reverse_lazy('oekaki:show')

    #f_name = request.POST.get('del')
    #f_name = f_name[1:]
    #os.remove(f_name)
    #return HttpResponse("Hello, world.")
    #return render(request, 'oekaki/show/del_image.html')
