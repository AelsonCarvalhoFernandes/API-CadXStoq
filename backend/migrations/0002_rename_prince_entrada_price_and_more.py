# Generated by Django 4.1.3 on 2022-11-10 11:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entrada',
            old_name='prince',
            new_name='price',
        ),
        migrations.RenameField(
            model_name='saida',
            old_name='prince',
            new_name='price',
        ),
    ]
