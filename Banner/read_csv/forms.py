from django import forms
from .models import Banner

class ImportForm(forms.ModelForm):
    class Meta:
        model = Banner
        fields = ['url','shows']