# Generated by Django 3.0.8 on 2021-06-27 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='گروه_اموزشی',
            name='status',
            field=models.CharField(choices=[('کاردانی', 'کاردانی'), ('کارشناسی', 'کارشناسی'), ('کاردانی و کارشناسی', 'کاردانی و کارشناسی')], default='کاردانی و کارشناسی', max_length=100),
        ),
    ]