# Generated by Django 4.1 on 2022-08-22 15:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Details', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='departmant',
            old_name='deparment',
            new_name='department',
        ),
        migrations.RenameField(
            model_name='students',
            old_name='deparment',
            new_name='department',
        ),
    ]
