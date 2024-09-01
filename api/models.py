from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    # Add any additional fields you want for your user model

    def __str__(self):
        return self.email
