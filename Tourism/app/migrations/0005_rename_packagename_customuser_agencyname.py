# Generated by Django 5.0.1 on 2024-01-26 15:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_customuser_packagename'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='packageName',
            new_name='agencyName',
        ),
    ]
