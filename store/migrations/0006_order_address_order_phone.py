# Generated by Django 4.1.4 on 2022-12-12 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0005_order"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="address",
            field=models.CharField(blank=True, default="", max_length=50),
        ),
        migrations.AddField(
            model_name="order",
            name="phone",
            field=models.CharField(blank=True, default="", max_length=50),
        ),
    ]
