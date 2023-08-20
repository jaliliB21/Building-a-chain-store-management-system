from django.db import models

from users.models import CustomUser

class News(models.Model):
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=255)
    text = models.TextField()
    news_image = models.ImageField(upload_to='meida/images/news', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(CustomUser, related_name='news', on_delete=models.CASCADE)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self) -> str:
        return self.title