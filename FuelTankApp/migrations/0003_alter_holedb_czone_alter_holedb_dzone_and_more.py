# Generated by Django 4.1.7 on 2023-09-26 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FuelTankApp', '0002_alter_holedb_azone_alter_holedb_bzone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='holedb',
            name='czone',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='holedb',
            name='dzone',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='holedb',
            name='ezone',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='holedb',
            name='fzone',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='holedb',
            name='gzone',
            field=models.CharField(max_length=10),
        ),
    ]
