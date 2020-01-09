from django import forms

from books.models import Book

class BookModelForm(forms.ModelForm):
	class Meta:
		model = Book
		fields = ['title','authors','publisher','publication_date',]
