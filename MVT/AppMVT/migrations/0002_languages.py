# Generated by Django 4.1 on 2022-08-30 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppMVT', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Languages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(max_length=50)),
                ('text', models.CharField(max_length=400)),
            ],
        ),
    ]