from django.db import models

# Create your models here.
class UserProfile(models.Model):
    user_id = models.CharField(
        max_length=100,
        primary_key=True
        )
    email = models.EmailField()
    uuid = models.UUIDField()
    timeout = models.DateTimeField()

    def __str__(self):
        return self.user_id
    class Meta:
        verbose_name = 'ユーザー情報一時保存'