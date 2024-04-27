from django_filters import FilterSet, DateFilter, ModelChoiceFilter, CharFilter
from .models import Post, Author
from django import forms


class PostFilter(FilterSet):
    add_time = DateFilter(widget=forms.DateInput(attrs={'type': 'date'}),
                          label='Дата',
                          lookup_expr='date__gte')

    author = ModelChoiceFilter(empty_label='Все авторы',
                               label='Автор',
                               queryset=Author.objects.all()
                               )
    text = CharFilter(label='Текст',
                      lookup_expr='icontains')

    class Meta:
        model = Post
        fields = ['text', 'author', 'add_time']


