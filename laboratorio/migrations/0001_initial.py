# Generated by Django 4.1.1 on 2024-12-08 22:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Laboratorio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('ciudad', models.CharField(blank=True, max_length=100, null=True)),
                ('pais', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('f_fabricacion', models.DateField()),
                ('p_costo', models.DecimalField(decimal_places=2, max_digits=12)),
                ('p_venta', models.DecimalField(decimal_places=2, max_digits=12)),
                ('laboratorio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='laboratorio.laboratorio')),
            ],
        ),
        migrations.CreateModel(
            name='DirectorGeneral',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('especialidad', models.CharField(blank=True, max_length=100, null=True)),
                ('laboratorio', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='laboratorio.laboratorio')),
            ],
        ),
    ]
