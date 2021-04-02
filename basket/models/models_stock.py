from datetime import datetime
from django.db import models

class Shopping_ListModel(models.Model):
    user_id = models.CharField(
        max_length=100
        )
    list_name = models.CharField(
        max_length=100
        )
    memo = models.CharField(
        max_length=200,
        blank=True,
        null=True
        )
    created_date = models.DateTimeField(
        default=datetime.now()
        )
    modified_date = models.DateTimeField(
        default=datetime.now()
        )

    def __str__(self):
        return self.list_name
    class Meta:
        verbose_name = '買い物リスト名'

class ProductModel(models.Model):
    list_name = models.ForeignKey(
        Shopping_ListModel,
        on_delete=models.CASCADE
        )
    name = models.CharField(
        max_length=100
        )
    quantity = models.CharField(
        max_length=100
        )

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'リスト項目'