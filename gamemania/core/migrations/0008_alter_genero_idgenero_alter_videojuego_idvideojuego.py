# Generated by Django 4.2.5 on 2023-09-20 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_genero_descripcion_genero_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genero',
            name='idGenero',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='videojuego',
            name='idVideojuego',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
