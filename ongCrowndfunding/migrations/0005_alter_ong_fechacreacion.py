# Generated by Django 4.1.2 on 2024-10-16 23:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ongCrowndfunding', '0004_alter_ong_estado_alter_ong_fechacreacion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ong',
            name='fechaCreacion',
            field=models.DateTimeField(default=datetime.datetime(2024, 10, 16, 20, 53, 25, 65415)),
        ),
    ]
