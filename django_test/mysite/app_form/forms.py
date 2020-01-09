from django import forms

class ContactForm(forms.Form):
	subject = forms.CharField(max_length = 100)
	email = forms.EmailField(required=False)
	message = forms.EmailField()

# from app_form.forms import *
# c = ContactForm()
# c.as_p()
# c.as_ul()
class ContactForm2(forms.Form):
    age = forms.IntegerField()
    nationality = forms.CharField()
    captcha_answer = forms.IntegerField(label='2 + 2', label_suffix=' =')

class CommentForm(forms.Form):
    name = forms.CharField(initial='Your name')
    url = forms.URLField(initial='http://')
    comment = forms.CharField()

import datetime
class DateForm(forms.Form):
    day = forms.DateField(initial=datetime.date.today)
    workdays = forms.ChoiceField(required=False, choices=(['1'], ['2']))
    # workdays = forms.ChoiceField(required=False, choices=(['1','label1'],['2','lable2'],['3','lable3']))

class HelpTextContactForm(forms.Form):
    subject = forms.CharField(max_length=100, help_text='100 characters max.')
    message = forms.CharField()
    sender = forms.EmailField(help_text='A valid email address, please.')
    cc_myself = forms.BooleanField(required=False)

from django.core.validators import RegexValidator

class PhoneField(forms.MultiValueField):
    def __init__(self, *args, **kwargs):
        # Define one message for all fields.
        error_messages = {
            'incomplete': 'Enter a country calling code and a phone number.',
        }
        # Or define a different message for each field.
        fields = (
            forms.CharField(
                error_messages={'incomplete': 'Enter a country calling code.'},
                validators=[
                    RegexValidator(r'^[0-9]+$', 'Enter a valid country calling code.'),
                ],
            ),
            forms.CharField(
                error_messages={'incomplete': 'Enter a phone number.'},
                validators=[RegexValidator(r'^[0-9]+$', 'Enter a valid phone number.')],
            ),
            forms.CharField(
                validators=[RegexValidator(r'^[0-9]+$', 'Enter a valid extension.')],
                required=False,
            ),
        )
        super(PhoneField, self).__init__(
            error_messages=error_messages, fields=fields,
            require_all_fields=False, *args, **kwargs
        )

CHOICES = (('1', 'A'), ('2', 'B'), ('3', 'C'))
BIRTH_YEAR_CHOICES = ('1980', '1981', '1982')
FAVORITE_COLORS_CHOICES = (
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
)

from django.contrib.admin.widgets import AdminDateWidget
import datetime
from django.utils import timezone
class MultipleChoiceForm(forms.Form):
    name = forms.CharField(max_length=500)
    choice = forms.ChoiceField(choices=[(1, 'Mon'), (2, 'Tue')])
    choice_field = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
    workdays = forms.MultipleChoiceField(choices=[(1, 'Mon'), 
        (2, 'Tue'),
        (3, 'Wed'),
        (4, 'Thur'),
        (5, 'Fri'),
        (6, 'Sat'),
        (7, 'Sun'),
        (8, 'Mon'),
        ])
    typedchoice = forms.TypedChoiceField(choices=CHOICES, coerce=int)
    typed_multichoice = forms.TypedMultipleChoiceField(choices=CHOICES, coerce=int)
    combo = forms.ComboField(fields=[forms.CharField(max_length=20), forms.EmailField()]) 
    boolfield = forms.TypedChoiceField(
                       coerce=lambda x: x == 'True',
                       choices=((False, 'False'), (True, 'True')),
                       widget=forms.RadioSelect
                    )
    phonefield = PhoneField() 
    birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    initialed_birth_year = forms.DateField(widget=forms.SelectDateWidget(),initial=timezone.now())
    favorite_colors = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=FAVORITE_COLORS_CHOICES,
    )    
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'special'}))
    url = forms.URLField()
    comment = forms.CharField(widget=forms.TextInput(attrs={'size': '40'}))
    myAdminDateWidget = forms.DateField(widget = AdminDateWidget())


class AdminDateForm(forms.Form):
    myAdminDateWidget = forms.DateField(widget = AdminDateWidget())
    