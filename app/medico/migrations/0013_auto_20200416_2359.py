# Generated by Django 3.0.5 on 2020-04-17 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medico', '0012_auto_20200416_2355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medico',
            name='foto',
            field=models.ImageField(blank=True, upload_to='fotos/1587092360.6734097'),
        ),
    ]
