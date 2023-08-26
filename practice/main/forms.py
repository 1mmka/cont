from dataclasses import field
from django.forms import ModelForm
from main.models import Image

class ImageForm(ModelForm):
    class Meta:
        model = Image
        fields = ('image',)