from django import forms
from .models import Post

"""
user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
title = models.CharField(max_length=120)
slug = models.SlugField(unique=True)
image = models.ImageField(upload_to=upload_location, 
		null=True, 
		blank=True, 
		# width_field="width_field", 
		# height_field="height_field"
		)
height_field = models.IntegerField(default=0)
width_field = models.IntegerField(default=0)
content = models.TextField()
draft = models.BooleanField(default=False)
publish = models.DateField(auto_now=False, auto_now_add=False)
updated = models.DateTimeField(auto_now=True, auto_now_add=False)
timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
"""

class PostModelForm(forms.ModelForm):
	# date_field = forms.DateField(initial='2010-01-20', widget=forms.SelectDateWidget(years=YEARS))
	# title = forms.CharField(
	# 		max_length=120, 
	# 		help_text='some help text',
	# 		error_messages={
	# 			"required" : "The title field is required."
	# 		}
	# 	)
	class Meta:
		model = Post
		fields = [
		"user",
		"title",
		"slug",
		]

		labels = {
			"title" : "This is title label",
			"slug" : "This is slug",
		}
		help_texts = {
			"title" : "This is title label",
			"slug" : "This is slug text",
		}

		error_messages = {
			# "title": {
			# 	"max_length" : "This is too long",
			# 	"required" : "This title field is required",
			# },
			"slug": {
				"max_length" : "This is too long",
				"required" : "This slug field is required",
				# "unique" : "This slug field must be required",
			},

		}

	def __init__(self, *args, **kwargs):
		super(PostModelForm, self).__init__(*args, **kwargs)
		self.fields["title"].widget=forms.Textarea()
		self.fields["title"].error_messages = {
			"max_length" : "This is title long",
			"required" : "This title field is required",
			}
		self.fields["slug"].error_messages = {
			"max_length" : "This is too long",
			"required" : "This slug field is required",
			}

		for field in self.fields.values():
			field.error_messages = {
				'required' : "You know, {fieldname} is required".format(fieldname=field.label)
			}

		# exclude = ["height_field"]







	# def clean_title(self, *args, **kwargs):
	# 	title = self.cleaned_data.get("title")
	# 	print(title)
	# 	# raise forms.ValidationError("Nope")
	# 	return title

	# def save(self, commit=True, *args, **kwargs):
	# 	obj = super(PostModelForm, self).save(commit=False, *args, **kwargs)

	# 	# obj.title = "New title"
	# 	obj.publish = "2016-10-1"
	# 	obj.content = "Coming soon"
	# 	# from django.utils.text import slugify
	# 	# obj.title = slugify(obj.title)
	# 	if commit:
	# 		obj.save()
	# 	return obj


SOME_CHOICES = [
	('db-value', 'Display Value'),
	('db-value2', 'Display2 Value'),
	('db-value3', 'Display3 Value'),
	]

INTS_CHOICES = [tuple([x,x]) for x in range(0, 102)]
YEARS = [x for x in range(1980, 2031)]
class TestForm(forms.Form):
	date_field = forms.DateField(initial='2010-01-20', widget=forms.SelectDateWidget(years=YEARS))
	some_text = forms.CharField(label='Text', widget=forms.Textarea(attrs={"rows":3, "cols": 3}))
	choices = forms.CharField(label='Text', widget=forms.Select(choices=SOME_CHOICES)) # Select, RadioSelect, SelectMultiple, CheckboxSelectMultiple
	boolean = forms.BooleanField()
	integer = forms.IntegerField(initial=101, widget=forms.Select(choices=INTS_CHOICES))
	email = forms.EmailField(min_length=10)

	def __init__(self, user=None, *args, **kwargs):
		super(TestForm, self).__init__(*args, **kwargs)
		print(user)
		if user:
			self.fields["some_text"].initial= user.username

	def clean_integer(self, *args, **kwargs):
		integer = self.cleaned_data.get("integer")
		if integer < 10:
			raise forms.ValidationError("The integer must be greater than 10")
		return integer

	def clean_some_text(self, *args, **kwargs):
		some_text = self.cleaned_data.get("some_text")
		if len(some_text) < 10:
			raise forms.ValidationError("Ensure the text is greater than 10 characters")
		return some_text

