# Generated by Django 4.2.5 on 2023-09-21 01:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_genero_imagen_alter_videojuego_imagen'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('idCategoria', models.AutoField(primary_key=True, serialize=False)),
                ('nombreCategoria', models.CharField(max_length=50, verbose_name='Nombre de la Categoría')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='img/')),
            ],
        ),
        migrations.RemoveField(
            model_name='videojuego',
            name='genero',
        ),
        migrations.DeleteModel(
            name='Genero',
        ),
        migrations.AddField(
            model_name='videojuego',
            name='categoria',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.categoria'),
        ),
    ]
