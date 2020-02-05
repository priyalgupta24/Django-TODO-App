from django.db import models

# Create your models here.

class todo_list(models.Model):
    todo=models.CharField(max_length=100)
    status=models.BooleanField()
