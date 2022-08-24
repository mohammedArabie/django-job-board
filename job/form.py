from dataclasses import field
from django import forms
from .models import Apply, Job

class ApplyForm (forms.ModelForm):
    class Meta :
        model=Apply
        fields=['name','email','cv','web_site','cover_letter']

class JobForm(forms.ModelForm):
    class Meta:
        model=Job
        fields='__all__'
        exclude=('owner','slug')