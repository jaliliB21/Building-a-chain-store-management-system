from django.db import models

class Store(models.Model):
    name = models.CharField(max_length=70)
    manager = models.CharField(max_length=50)
    address = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self) -> str:
        return self.name