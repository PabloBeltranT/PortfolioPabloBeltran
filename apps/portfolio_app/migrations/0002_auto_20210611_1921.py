# Generated by Django 3.2 on 2021-06-11 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('tags', models.CharField(max_length=200)),
                ('date', models.DateField(default=None)),
                ('content', models.CharField(max_length=1000)),
            ],
        ),
        migrations.AlterField(
            model_name='projects',
            name='description',
            field=models.CharField(max_length=500),
        ),
    ]
