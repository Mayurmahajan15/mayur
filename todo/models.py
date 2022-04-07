from django.db import models
from django.contrib.auth.models import User

# Create your models here
class Todo(models.Model):
    title=models.CharField(max_length=255)
    description=models.TextField(max_length=255)
    name=models.CharField(max_length=200)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    

class Contact(models.Model):
    email=models.CharField(max_length=255)
    name=models.CharField(max_length=255)
    mobile=models.CharField(max_length=255)
    enquiry=models.CharField(max_length=255)