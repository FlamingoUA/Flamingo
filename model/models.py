from django.db import models


class Ticket(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    price = models.FloatField(default=0.0)
    flight_number = models.CharField(max_length=255, null=True, blank=True)
    booking_class = models.CharField(max_length=25, null=True, blank=True)
    date = models.DateField(auto_now_add=True)
    flight_route = models.CharField(max_length=255, null=True, blank=True)
    flight_route_time = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'ticket'
