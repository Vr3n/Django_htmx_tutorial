from django import forms
from .models import Book, Author


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = (
            'title',
            'number_of_pages'
        )

BookFormSet = forms.models.inlineformset_factory(
    Author, # Parent model.
    Book, # Child Model.
    form=BookForm, # Form
    min_num=1, # Minimum number of forms that must be filled in
    extra=1, # number of empty forms to display
    can_delete=False # show a checkbox in each form to delete the row
)