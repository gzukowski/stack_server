# in your app's models.py
from django.contrib.auth.models import AbstractUser, Group, Permission, UserManager, BaseUserManager
from django.db import models


class CustomUserManager(BaseUserManager):
    def _create_user(self, username, password):
        if not password:
            raise ValueError('Password is not provided')

        user = self.model(
            username = username,
            wins = 0,
            losses = 0
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, password):
        return self._create_user(username, password)

    def create_superuser(self, username, password):
        return self._create_user(username, password)



class CustomUser(AbstractUser):
    STATUS = (
        ('regular', 'regular'),
    )

    wins = models.PositiveIntegerField(default=0)
    losses = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=100, choices=STATUS, default='regular')

    def __str__(self):
        return self.username
