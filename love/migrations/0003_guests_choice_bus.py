# Generated by Django 4.1.3 on 2023-04-19 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("love", "0002_delete_gifts_guests_bus"),
    ]

    operations = [
        migrations.AddField(
            model_name="guests",
            name="choice_bus",
            field=models.CharField(
                blank=True, choices=[{"bus", "BUS"}], max_length=4, null=True
            ),
        ),
    ]
