#This is Form File
import decimal

from django import forms
from django.db.models import Value
from django.forms import fields
from .models import StudentState, Availability
from decimal import Decimal


class add_form(forms.ModelForm):
    class Meta:
        model=StudentState
        fields=['name','topics','mastery','av_time']
    name=forms.CharField(
        label='Your Name',
        help_text='Enter Your Full Name')
    topics=forms.CharField(
        label='Topic(s)',
        help_text='Topics you want to learn')
    mastery=forms.DecimalField(
        label='Mastery',
        help_text='How much you know about topic(s)(%)')
    av_time=forms.IntegerField()
    def clean_mstry(self):
        Value =self.cleaned_data['mastery']
        return Value / Decimal('100')



class AvailabilityForm(forms.ModelForm):
    class Meta:
        model = Availability
        fields = ['day', 'hours_free']

    def clean_hours_free(self):
        hours = self.cleaned_data['hours_free']
        if hours > 24:
            raise forms.ValidationError("There can't be more than 24 hours in a day.")
        if hours < 0:
            raise forms.ValidationError("Hours can't be negative.")
        return hours