from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    """Modelo de Usuario
    
    Extiende desde Django Abstract User.
    """

    username = models.CharField(
        max_length=125,
        null=True,
        blank=True
    )

    email = models.EmailField(
        unique=True,
        error_messages={
            'unique': 'El correo electrónico ya existe.'
        }
    )
    created = models.DateField(auto_now_add=True)
    modified = models.DateField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        db_table = 'user'