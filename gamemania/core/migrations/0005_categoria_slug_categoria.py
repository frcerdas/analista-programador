# Generated by Django 4.2.5 on 2023-09-21 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_categoria_remove_videojuego_genero_delete_genero_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='slug_categoria',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]