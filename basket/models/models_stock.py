from django.db import models

class Shopping_ListNameModel(models.Model):
    user_id = models.CharField(
        max_length=100
        )
    list_name = models.CharField(
        max_length=100
        )

class Shopping_ListModel(models.Model):
    list_name = models.ForeignKey(
        'Shopping_ListNameModel',
        on_delete=models.CASCADE
        )
    name = models.CharField(
        max_length=100
        )
    quantity = models.CharField(
        max_length=100
        )
    memo = models.CharField(
        max_length=200,
        blank=True,
        null=True
        )