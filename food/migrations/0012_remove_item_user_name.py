# Generated by Django 5.0.6 on 2024-10-25 10:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0011_alter_item_user_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='user_name',
        ),
    ]
