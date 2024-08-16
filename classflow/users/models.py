from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Add additional fields here if needed



    # For example, you could also add a user bio or a profile picture
    # bio = models.TextField(null=True, blank=True)
    # profile_pic = models.ImageField(upload_to='profile_pics/', null=True, blank=True)

    # Any custom methods you need can be added here

    def __str__(self):
        return self.username
