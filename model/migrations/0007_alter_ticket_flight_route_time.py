# Generated by Django 4.1.1 on 2022-10-16 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0006_alter_ticket_arrival_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='flight_route_time',
            field=models.TimeField(blank=True, max_length=255, null=True),
        ),
    ]
