# Generated by Django 3.0.5 on 2020-04-17 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atendente', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atendente',
            name='foto',
            field=models.ImageField(blank=True, upload_to='fotos/1587091277.3469899'),
        ),
    ]
