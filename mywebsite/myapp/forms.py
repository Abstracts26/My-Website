from django.forms import ModelForm
from .models import *

class CUmodel(ModelForm):
    class Meta:
        model = MobilePhone
        fields = '__all__'