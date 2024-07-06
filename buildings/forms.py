from django import forms
from django.forms import TextInput, EmailInput, ModelForm


class TellSomething(forms.Form):
	UserInput= forms.CharField(required=True, max_length=200,
		   widget=TextInput({
		   	'placeholder': 'Tell us something',
		   	'style': 'margin-right:20rem; height: 125px; ',
		   }))
	
