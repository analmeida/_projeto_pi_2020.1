# Generated by Django 3.0.5 on 2020-05-03 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atendente', '0029_auto_20200502_1531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atendente',
            name='foto',
            field=models.ImageField(blank=True, upload_to='fotos/1588471436.738998'),
        ),
    ]