# Generated by Django 3.1.7 on 2021-02-21 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('therapists', '0002_auto_20210221_1941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='therapist',
            name='FIO',
            field=models.TextField(max_length=800),
        ),
    ]