# Generated by Django 3.2 on 2021-04-21 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datacenter', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mark',
            name='created',
            field=models.DateTimeField(null=True, verbose_name='дата и время'),
        ),
    ]
