# Generated by Django 2.1.2 on 2019-05-26 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='direccion',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='persona',
            name='telefono',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
