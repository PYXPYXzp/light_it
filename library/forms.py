from django import forms

from library.models import Book, Author


class AddBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(AddBookForm, self).__init__(*args, **kwargs)
        # self.fields['author'].widget.attrs.update({'class': 'form-control'})
        for key, field in self.fields.iteritems():
            field.widget.attrs.update({'class': 'form-control'})


class AddAuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(AddAuthorForm, self).__init__(*args, **kwargs)
        for key, field in self.fields.iteritems():
            field.widget.attrs.update({'class': 'form-control'})
