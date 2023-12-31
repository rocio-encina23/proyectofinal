# Generated by Django 4.2 on 2023-12-02 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recetas', '0004_huerta'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tragos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=64)),
                ('articulo', models.CharField(max_length=400)),
                ('ingredientes', models.TextField()),
                ('pasos', models.TextField()),
                ('imagenLibro', models.ImageField(blank=True, null=True, upload_to='imagenes/')),
            ],
        ),
    ]
