# Generated by Django 4.0.5 on 2022-07-03 13:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_allergy_table'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='allergy',
            table='allergies',
        ),
    ]
