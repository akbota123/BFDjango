from django import forms
from main.models import Task, Author

class AuthorForm(forms.ModelForm):
    class Meta:
        model=Author
        fields=('first_name', 'email')