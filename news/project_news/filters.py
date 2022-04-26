from django.forms import DateInput
import django_filters


class PostFilter(django_filters.FilterSet):

    text= django_filters.CharFilter(field_name='text', lookup_expr='icontains', label='Текст')
    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains', label='Заголовок')
    date = django_filters.DateFilter(field_name='dateCreation', widget=DateInput(attrs={'type': 'date'}), lookup_expr='gt', label='Новее этой даты')




