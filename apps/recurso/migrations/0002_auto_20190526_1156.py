# Generated by Django 2.1.2 on 2019-05-26 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recurso', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recurso',
            name='categoria',
            field=models.CharField(choices=[('AC', 'Accesorios de computo'), ('AS', 'Accesorios de seguridad')], max_length=50),
        ),
    ]
