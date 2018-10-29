from django.contrib import admin
from main.models import User, Restaurant, Dish, Review
# Register your models here.

admin.site.register(Restaurant)
admin.site.register(Dish)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    l=('name')
