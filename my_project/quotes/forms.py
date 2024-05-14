from django.db.models import Q
from django.forms import CharField, TextInput, ModelForm, ModelChoiceField, Select, ChoiceField, \
    ModelMultipleChoiceField, SelectMultiple, DateField
from .models import Quote, Author, Tag


class QuotesForm(ModelForm):
    quote = CharField(max_length=300, min_length=3, required=True, widget=TextInput(attrs={'class': 'form-control'}))
    author = ModelChoiceField(queryset=Author.objects.all(), required=True, widget=Select(attrs={'class': 'form-control'}))
    tags = ModelMultipleChoiceField(queryset=Tag.objects.all(), required=False, widget=SelectMultiple(attrs={'class': 'form-control'}))

    class Meta:
        model = Quote
        fields = ('quote', 'tags', 'author')

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(QuotesForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['author'].queryset = Author.objects.filter(Q(user=user) | Q(user=None))


class AuthorForm(ModelForm):
    fullname = CharField(max_length=16, min_length=3, required=True, widget=TextInput(attrs={'class': 'form-control'}))
    born_date = DateField(required=True, widget=TextInput(attrs={'class': 'form-control'}))
    born_location = CharField(max_length=16, min_length=3, required=True, widget=TextInput(attrs={'class': 'form-control'}))
    description = CharField(max_length=300, min_length=3, required=True, widget=TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Author
        fields = ('fullname', 'born_date', 'born_location', 'description')