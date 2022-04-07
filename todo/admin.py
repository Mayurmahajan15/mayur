from django.contrib import admin
from todo.models import Todo #admin can access our ap

# Register your models here.

admin.site.register(Todo) #admin can access our database
