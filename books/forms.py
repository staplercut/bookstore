from django import forms
from .models import Book, Author
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.widgets import SelectDateWidget
from django.utils.timezone import datetime
from django.utils import timezone


import string


class BookForm(forms.ModelForm):
    title = forms.CharField(label='Book title', required=True)

    class Meta:
        model = Book
        fields = ('title', 'author_input', 'isbn', 'publish_date', 'price')

    author_input = forms.ModelMultipleChoiceField(
        queryset=Author.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

    publish_date = forms.DateField(widget=SelectDateWidget(years=range(datetime.now().year, 1900, -1)), initial=timezone.now())

    # unique validation
    def clean_title(self):
        pre_title = self.cleaned_data['title']
        title = ' '.join(w.capitalize() for w in pre_title.translate(str.maketrans('', '', string.punctuation)).split())
        return title


