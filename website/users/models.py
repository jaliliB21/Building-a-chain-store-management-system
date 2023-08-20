from django.contrib.auth.models import AbstractUser
from django.db import models

from stores.models import Store

class Rol(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self) -> str:
        return self.name



class CustomUser(AbstractUser):

    profile_image = models.ImageField(upload_to='media/images/profile', null=True, blank=True)
    store = models.ForeignKey(Store, related_name='users', null=True, on_delete=models.CASCADE)
    job = models.CharField(max_length=20)
    rol = models.ForeignKey(Rol, related_name='users', null=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self) -> str:
        return self.username
