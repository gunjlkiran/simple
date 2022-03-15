
import email
from django.db import models

# Create your models here.
class student(models.Model):
    name=models.CharField(max_length=30,null=True)
    email=models.EmailField(null=True)
    address=models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.name
