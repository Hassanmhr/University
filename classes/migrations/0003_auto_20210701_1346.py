# Generated by Django 3.0.8 on 2021-07-01 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0002_auto_20210627_1649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='کلاس',
            name='number_class',
            field=models.CharField(max_length=100),
        ),
    ]