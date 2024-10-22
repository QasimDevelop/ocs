from django.db import models

# Create your models here.
class User(models.Model):
    id=models.BigAutoField(primary_key=True)
    usrName=models.TextField(max_length=30)
    pswd=models.TextField(max_length=30)