from django.db.models.fields import DateField
import django_filters
from django_filters.filters import ChoiceFilter
from accounts.models import *
from django_filters import DateFilter,CharFilter


class OrderFilter(django_filters.FilterSet):
    # #filtering with date
    # start_date = DateFilter(field_name ="date_created",lookup_expr='gte')
    # end_date = DateFilter(field_name ="date_created",lookup_expr='lte')
    note = CharFilter(field_name="note",lookup_expr='icontains')
    class Meta:
        model = Order
        fields = '__all__'
        exclude = ['customer','date_created']