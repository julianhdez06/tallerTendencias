# Generated by Django 5.1 on 2024-09-07 18:30

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='ticket',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='tickets.ticket'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='usuario',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='asunto',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tickets', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='estado',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='soporte',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='soporte_tickets', to=settings.AUTH_USER_MODEL),
        ),
    ]
