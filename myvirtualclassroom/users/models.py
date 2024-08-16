# users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Add additional fields here if required
    department = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.username
