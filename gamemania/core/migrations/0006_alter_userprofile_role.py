# Generated by Django 4.2.5 on 2023-09-20 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_userprofile_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='role',
            field=models.CharField(choices=[('admin', 'Administrador'), ('cliente', 'Cliente')], max_length=20, verbose_name='Rol'),
        ),
    ]
