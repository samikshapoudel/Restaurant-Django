from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class Custom_user(AbstractUser):
    phone_no = models.CharField(max_length=20)
    email = models.EmailField(unique=True)


