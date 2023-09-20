# Generated by Django 4.2.5 on 2023-09-20 20:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('idGenero', models.AutoField(primary_key=True, serialize=False)),
                ('nombreGenero', models.CharField(max_length=50, verbose_name='Nombre del Género')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='img/')),
            ],
        ),
        migrations.CreateModel(
            name='Videojuego',
            fields=[
                ('idVideojuego', models.AutoField(primary_key=True, serialize=False)),
                ('nombreVideojuego', models.CharField(max_length=50, verbose_name='Nombre del videojuego')),
                ('descripcion', models.TextField(blank=True, null=True, verbose_name='Descripcion del videojuego')),
                ('fechalanzamiento', models.DateField(blank=True, null=True, verbose_name='Fecha de lanzamiento del videojuego')),
                ('precio', models.IntegerField(verbose_name='Precio del videojuego')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='img/')),
                ('genero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.genero')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('admin', 'Administrador'), ('cliente', 'Cliente')], max_length=20, verbose_name='Rol')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
