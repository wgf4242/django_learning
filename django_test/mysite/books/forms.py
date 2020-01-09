from django import forms
from books.models import Book
class ContactForm(forms.Form):
	subject = forms.CharField(max_length=100)
	email = forms.EmailField(required=False, label='Your e-mail address')
	message = forms.CharField(widget=forms.Textarea)
	
	def clean_message(self):
		message = self.cleaned_data['message']
		num_words = len(message.split())
		if num_words < 4:
			raise forms.ValidationError("Not enough words!")
		return message


# class BookForm(forms.From):
# 	title = forms.CharField(label="名称", error_messages={"required" : " 这个必须填写"})
# 	authors = forms.CharField()
# 	publisher = forms.CharField()
# 	publication_date = forms.DateField()

class BookForm(forms.ModelForm):

	class Meta:
		model = Book
		exclude = ('id',)

