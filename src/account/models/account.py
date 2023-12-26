import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser

  
class User(AbstractUser):
    username = models.CharField(max_length=255, default=uuid.uuid4, unique=True)
    
    
    USERNAME_FIELD = 'username'
    
    def __str__(self):
        return self.username

    class Meta:
        ordering = ('-date_joined',)
        verbose_name = "User"
        verbose_name_plural = "Users"
        db_table = "user"
