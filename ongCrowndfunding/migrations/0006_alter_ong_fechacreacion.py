# Generated by Django 4.1.2 on 2024-10-16 23:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ongCrowndfunding', '0005_alter_ong_fechacreacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ong',
            name='fechaCreacion',
            field=models.DateTimeField(default=datetime.datetime(2024, 10, 16, 20, 54, 30, 851863)),
        ),
    ]
