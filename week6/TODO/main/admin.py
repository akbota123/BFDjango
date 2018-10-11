from django.contrib import admin
from main.models import Person, Task

# Register your models here.

admin.site.register(Task)

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display=('first_name', 'second_name', 'email')


