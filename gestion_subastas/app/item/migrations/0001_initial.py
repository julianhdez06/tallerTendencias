# Generated by Django 5.1.1 on 2024-09-07 16:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auction', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('descripcion', models.TextField()),
                ('precio_inicial', models.DecimalField(decimal_places=2, max_digits=10)),
                ('subasta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='auction.auction')),
            ],
        ),
    ]
