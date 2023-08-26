from typing import List
from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from main.forms import ImageForm
from main.models import Image
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
class ImgCreate(CreateView):
    template_name = 'index.html'
    form_class = ImageForm

    def post(self, request):
        image = Image.objects.create(image = request.FILES.get('image',''))
        image.save()
        return HttpResponseRedirect(reverse('list_view'),status=302,reason='check images')

class ImgList(ListView):
    model = Image
    template_name = 'list.html'
    context_object_name = 'images'