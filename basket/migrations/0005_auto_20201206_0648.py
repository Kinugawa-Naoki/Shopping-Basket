# Generated by Django 3.1.3 on 2020-12-06 06:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basket', '0004_shopping_listmodel_list_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shopping_ListNameModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('list_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='shopping_listmodel',
            name='memo',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='shopping_listmodel',
            name='list_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basket.shopping_listnamemodel'),
        ),
    ]
