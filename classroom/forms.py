from django import forms
from classroom.models import (Stude)

class StudeForm(forms.ModelForm):
    class Meta:
        model = Stude
        exclude = ['user']
