import datetime

from django import forms

from .models import Task

class DateInput(forms.DateInput):
    input_type = 'date'
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'place', 'match_date', 'description')

        labels = {
            'title': 'Tytuł',
            'place': 'Miejsce',
            'match_date': 'Data',
            'description': 'Opis'
        }

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'place': forms.TextInput(attrs={'class': 'form-control'}),
            'match_date': DateInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'})
        }

