# Generated by Django 4.0.3 on 2022-09-14 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0005_clientreview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientreview',
            name='review',
            field=models.TextField(blank=True),
        ),
    ]