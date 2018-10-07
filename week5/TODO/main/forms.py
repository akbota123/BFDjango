from django.forms import ModelForm
from django import forms
from .models import Person, Task

##class SearchListForm(forms.Form):
  ##  name = forms.CharField(max_length=100)

class TaskForm(ModelForm):
    class Meta:
        model=Task
        fields=('name_t', 'created', 'dueon', 'owner', 'mark')

