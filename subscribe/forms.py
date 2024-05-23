from django import forms

from django.utils.translation import gettext_lazy as _
from subscribe.models import Subscribe

# # validating field using django validator
# def validate_comma(value):
#     if "," in value:
#         raise forms.ValidationError("Invalid last name")

# # defining a form class
# class SubscribeForm(forms.Form):
#     first_name = forms.CharField(max_length=100, required=False ,label='Enter your First Name', help_text='Enter characters only')
#     last_name = forms.CharField(max_length=100, disabled=False, validators=[validate_comma])
#     email = forms.EmailField(max_length=100)

    # validating form field using django CLEAN object (clean_<field_name>)
    # def clean_first_name(self):
    #     data = self.cleaned_data['first_name']
    #     if ',' in data:
    #         raise forms.ValidationError('Invalid first name')
    #     return data

# converting models into form with django MODELFORM 
class SubscribeForm(forms.ModelForm):
    class Meta:
        model=Subscribe
        fields='__all__'
        # exclude = ('first_name',)
        # fields=['first_name', 'last_name', 'email']

        # adding custom labels
        labels = {
            'first_name' : _('Enter first name'),
            'last_name' : _('Enter last name'),
            'email' : _('Enter email'),
        }
        # help_texts = {'first_name':_('Enter character only')}

        error_messages = {
            'first_name': {
                'required': _('You cannot proceed without this field')
            },
        }