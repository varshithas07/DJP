from .models import Task
from django import forms

# need to define the form class
class TaskForm(forms.ModelForm):
    class Meta:
        model=Task
        fields="__all__"