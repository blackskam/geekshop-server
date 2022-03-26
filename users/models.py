from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now
from datetime import timedelta


class User(AbstractUser):
    image = models.ImageField(upload_to='users images', null=True,blank=True)
    activation_key = models.CharField(max_length=128,blank=True)
    activation_key_expires = models.DateTimeField(default=(now() + timedelta(hours=48)),null=True,blank=True)

    @property
    def is_activation_key_expires(self):
        try:
            if now() <= self.activation_key_expires:
                return False
        except Exception as e:
            pass
        return True


    def save_delete(self):
        self.is_active = False
        self.save()


