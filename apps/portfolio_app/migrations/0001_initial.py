# Generated by Django 3.2 on 2021-06-03 23:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(default='visible', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Visits',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_to', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='projects')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('url', models.CharField(max_length=20)),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio_app.status')),
                ('tags', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio_app.tags')),
            ],
        ),
    ]
