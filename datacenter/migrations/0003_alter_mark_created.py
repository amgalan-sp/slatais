# Generated by Django 3.2 on 2021-04-21 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datacenter', '0002_alter_mark_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mark',
            name='created',
            field=models.DateField(null=True, verbose_name='дата и время'),
        ),
    ]
