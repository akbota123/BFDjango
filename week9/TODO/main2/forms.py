from django.forms import ModelForm
from main2.models import TaskManager, Task, Author

class AuthorForm(ModelForm):
    class Meta:
        model=Author
        fields=('first_name', )
