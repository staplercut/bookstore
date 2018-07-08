from django import forms
from .models import Book, Author


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

    # unique validation
    def clean_title(self):
        pre_title = self.cleaned_data['title']
        title = ' '.join(w.capitalize() for w in pre_title.translate(str.maketrans('', '', string.punctuation)).split())
        return title


class AuthorForm(forms.ModelForm):
    name = forms.CharField(label='Name', required=True)

    class Meta:
        model = Author
        fields = ('name', 'tags')

    # unique validation
    def clean_name(self):
        pre_name = self.cleaned_data['name']
        name = ' '.join(w.capitalize() for w in pre_name.translate(str.maketrans('', '', string.punctuation)).split())
        return name
