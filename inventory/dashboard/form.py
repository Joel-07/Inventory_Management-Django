from django import forms
from django.forms import fields
from .models import balance


class searchform(forms.ModelForm):
    class Meta:
        model=balance
        fields=['pid','warehouse']
