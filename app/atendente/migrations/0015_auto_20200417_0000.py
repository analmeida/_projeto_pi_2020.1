# Generated by Django 3.0.5 on 2020-04-17 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atendente', '0014_auto_20200416_2359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atendente',
            name='foto',
            field=models.ImageField(blank=True, upload_to='fotos/1587092425.257651'),
        ),
    ]
