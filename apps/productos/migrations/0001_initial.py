# Generated by Django 3.2.6 on 2022-10-01 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('codigo', models.CharField(max_length=50, unique=True, verbose_name='Codio de Barras')),
                ('nombre', models.CharField(max_length=150, unique=True, verbose_name='Nombre de Producto')),
                ('costo', models.IntegerField(verbose_name='Costo de compra')),
                ('precio', models.IntegerField(verbose_name='Precio de venta')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('modified_date', models.DateField(auto_now=True, verbose_name='Fecha de Modificación')),
                ('deleted_date', models.DateField(auto_now=True, verbose_name='Fecha de Eliminación')),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
            },
        ),
    ]
