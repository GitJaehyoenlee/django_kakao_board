from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    image = models.ImageField(upload_to='profile/', blank=True, null=True)
    git_address = models.TextField()