# Generated by Django 5.0.2 on 2024-03-06 19:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppCerveza', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ginebra',
            old_name='regionOrigen',
            new_name='sabor',
        ),
    ]
