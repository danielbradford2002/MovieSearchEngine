from django import forms
from django.forms import ModelForm, TextInput

class TitleForm(forms.Form):
    title = forms.CharField(label='Movie Title', max_length=200)
