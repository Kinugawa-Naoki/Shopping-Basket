from django.db import models

# Create your models here.
class UserProfile(models.Model):
    user_id = models.CharField(
        max_length=100,
        primary_key=True
    )
    email = models.EmailField()
    password = models.CharField(
        max_length=100
    )
    uuid = models.UUIDField()
    timeout = models.DateTimeField()