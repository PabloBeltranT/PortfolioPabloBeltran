# Generated by Django 3.2 on 2021-05-23 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=100)),
                ('precio', models.CharField(max_length=5)),
                ('estado', models.BooleanField(default=False)),
                ('imagen', models.ImageField(null=True, upload_to='aguachiles')),
            ],
        ),
    ]