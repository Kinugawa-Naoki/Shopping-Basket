# Generated by Django 3.1.3 on 2020-12-28 10:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basket', '0006_auto_20201206_0736'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='shopping_listmodel',
            options={'verbose_name': 'リスト項目'},
        ),
        migrations.AlterModelOptions(
            name='shopping_listnamemodel',
            options={'verbose_name': '買い物リスト名'},
        ),
        migrations.AlterModelOptions(
            name='userprofile',
            options={'verbose_name': 'ユーザー情報一時保存'},
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='password',
        ),
    ]