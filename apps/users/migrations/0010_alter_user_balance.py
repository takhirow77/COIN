# Generated by Django 5.0.1 on 2024-06-06 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_alter_user_balance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='balance',
            field=models.PositiveIntegerField(default=4, verbose_name='Баланс'),
        ),
    ]
