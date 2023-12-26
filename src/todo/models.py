from django.db import models

from core.utils.base_model import BaseModel


class Task(BaseModel):
    user = models.ForeignKey('account.User', on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=255)
    memo = models.TextField()
    is_completed = models.BooleanField(default=False)
    is_important = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.title} - {self.memo}"
