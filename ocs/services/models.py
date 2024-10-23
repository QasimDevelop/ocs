from django.db import models

# Create your models here.
class User(models.Model):
    usrName=models.CharField(max_length=30)
    email=models.EmailField(primary_key=True)
    pswd=models.CharField(max_length=30)
    def __str__(self) -> str:
        return self.email