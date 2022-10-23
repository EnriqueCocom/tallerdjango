# Generated by Django 4.1.2 on 2022-10-20 22:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=30, null=True, unique=True)),
                ('email', models.EmailField(blank=True, max_length=60, null=True, verbose_name='email')),
                ('phone', models.CharField(blank=True, max_length=16, null=True, unique=True)),
            ],
            options={
                'verbose_name': 'Mis departamentos',
            },
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('empresa', models.CharField(blank=True, max_length=100, null=True)),
                ('phone', models.CharField(max_length=10, unique=True)),
                ('email', models.EmailField(max_length=60, verbose_name='email')),
            ],
            options={
                'verbose_name': 'Mis proveedores',
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('cantidad', models.IntegerField(default=0)),
                ('proveedor', models.ForeignKey(db_column='proveedorid', on_delete=django.db.models.deletion.CASCADE, to='app.proveedor')),
            ],
            options={
                'verbose_name': 'Mis productos',
            },
        ),
    ]
