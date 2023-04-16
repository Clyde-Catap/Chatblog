from django.db import models
from  django.utils import timezone
from  django.contrib.auth.models import User


class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    def __str__(self):
        return self.username

