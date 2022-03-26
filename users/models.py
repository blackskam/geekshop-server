from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now
from datetime import timedelta

class User(AbstractUser):
    image = models.ImageField(upload_to='users images', null=True,blank=True)

    def save_delete(self):
        self.is_active = False
        self.save()


