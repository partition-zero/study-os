#This is Form File
from django import forms
from django.forms import fields
from .models import StudentState
class S_form(forms.ModelForm):
    class Meta:
        model=StudentState
        fields='__all__'
