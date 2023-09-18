from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField(max_length=254, unique=True)
    location = models.CharField(max_length=60, blank=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
