# Generated by Django 2.1.15 on 2021-08-26 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
