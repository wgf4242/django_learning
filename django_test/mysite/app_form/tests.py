import datetime
from django.utils import timezone
from django.test import TestCase
from django import forms

# python manage.py test polls

class FormMethodTests(TestCase):

	# python manage.py test app_form.tests.FormMethodTests.test_error1
    def test_error1(self):
    	generic = forms.CharField()
    	generic.clean('')
    	# ValidationError: ['This field is required.']
    def test_error2(self):
    	name = forms.CharField(error_messages={'required': 'Please enter your name'})
    	name.clean('')
    	# ValidationError: ['Please enter your name']