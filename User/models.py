from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    role_choices = (
        ('sme', ('SME')),
        ('funder', ('Funder')),
        ('admin', ('admin')),
    ) 
    
    user_role = models.CharField(
        max_length=32,
        choices=role_choices,
        default='',
    )





