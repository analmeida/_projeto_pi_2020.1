# Generated by Django 3.0.5 on 2020-04-15 00:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Atendente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('sexo', models.CharField(max_length=1)),
                ('data_nascimento', models.DateField()),
                ('cpf', models.CharField(max_length=20, unique=True)),
                ('rg', models.CharField(max_length=20, unique=True)),
                ('email', models.EmailField(max_length=254)),
                ('foto', models.ImageField(blank=True, upload_to='fotos/')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]