from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    occupation = models.CharField(max_length=200, default='unkown')
    bio = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.user.username


