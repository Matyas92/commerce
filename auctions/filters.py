

import django_filters

from .models import *

class OrderFilter(django_filters.FilterSet):
    class Meta:
        model = CreateListing
        fields = '__all__'
        exclude = ['user','title','description','startingBid','url','picture','closing','currentbidder']