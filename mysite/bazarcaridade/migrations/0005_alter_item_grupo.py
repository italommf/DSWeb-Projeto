# Generated by Django 4.0.6 on 2023-07-03 17:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bazarcaridade', '0004_item_grupo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='grupo',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='bazarcaridade.evento'),
        ),
    ]
