# Generated by Django 3.1.3 on 2020-12-29 14:27

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shopping_ListModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=100)),
                ('list_name', models.CharField(max_length=100)),
                ('memo', models.CharField(blank=True, max_length=200, null=True)),
                ('created_date', models.DateTimeField(default=datetime.datetime(2020, 12, 29, 23, 27, 15, 105742))),
                ('modified_date', models.DateTimeField(default=datetime.datetime(2020, 12, 29, 23, 27, 15, 105771))),
            ],
            options={
                'verbose_name': '買い物リスト名',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254)),
                ('uuid', models.UUIDField()),
                ('timeout', models.DateTimeField()),
            ],
            options={
                'verbose_name': 'ユーザー情報一時保存',
            },
        ),
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('quantity', models.CharField(max_length=100)),
                ('list_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basket.shopping_listmodel')),
            ],
            options={
                'verbose_name': 'リスト項目',
            },
        ),
    ]
