import django_filters
from .models import *
from django_filters import CharFilter

class MobileFilter(django_filters.FilterSet):
    
    brand = CharFilter(field_name='brand', lookup_expr='icontains')
    class Meta:
        model = MobilePhone
        fields = '__all__'
        exclude = ['brand','model','description','price','date_created']