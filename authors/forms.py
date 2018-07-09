from django import forms
from .models import Author

import string


class AuthorForm(forms.ModelForm):
    name = forms.CharField(label='Name', required=True)

    class Meta:
        model = Author
        fields = ('name',)

    # unique validation
    def clean_name(self):
        pre_name = self.cleaned_data['name']
        name = ' '.join(w.capitalize() for w in pre_name.translate(str.maketrans('', '', string.punctuation)).split())
        return name

