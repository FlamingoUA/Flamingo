# Generated by Django 4.1.1 on 2022-10-07 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0003_alter_ticket_arrival_time_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='currency',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]