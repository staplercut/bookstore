from django import forms
from .models import Book, Author
from logs.models import BookChangeLogs
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

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get('author_input') is not None:
            fields = Book._meta.get_fields()
            if self.instance.pk is not None:
                model_id = self.instance.pk
                action = 'create' if model_id is None else 'edit'
                new_instance = {
                    'id': model_id,
                    'title': cleaned_data.get('title'),
                    'authors': list(cleaned_data.get('author_input')),
                    'isbn': cleaned_data.get('isbn'),
                    'publish_date': cleaned_data.get('publish_date'),
                    'price': cleaned_data.get('price'),
                }
                prev_instance = Book.objects.get(pk=self.instance.pk)
                for field in fields:
                    field_name = field.name
                    if field_name is not 'authors':
                        if new_instance[field_name] != getattr(prev_instance, field_name):
                            data = new_instance[field_name]
                            entry = BookChangeLogs.objects.create(model_id=model_id, field=field_name, data=data, action=action,
                                                                  timestamp=timezone.now())
                            entry.save()
