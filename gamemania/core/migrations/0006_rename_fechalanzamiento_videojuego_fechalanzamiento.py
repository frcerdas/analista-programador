# Generated by Django 4.2.5 on 2023-10-01 21:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_categoria_slug_categoria'),
    ]

    operations = [
        migrations.RenameField(
            model_name='videojuego',
            old_name='fechalanzamiento',
            new_name='fechaLanzamiento',
        ),
    ]