# Generated by Django 3.1.1 on 2021-04-02 01:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basket', '0002_auto_20201230_1117'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodel',
            name='user_id',
            field=models.CharField(default='AnonymousUser', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='shopping_listmodel',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 2, 10, 43, 11, 471469)),
        ),
        migrations.AlterField(
            model_name='shopping_listmodel',
            name='modified_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 2, 10, 43, 11, 471501)),
        ),
    ]
