# Generated by Django 4.0.6 on 2023-07-03 17:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bazarcaridade', '0005_alter_item_grupo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='grupo',
            new_name='evento',
        ),
    ]
