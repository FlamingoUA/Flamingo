from django.db import models


class Ticket(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    price = models.FloatField(default=0.0)
    currency = models.CharField(max_length=10, null=True, blank=True)
    flight_number = models.CharField(max_length=255, null=True, blank=True)
    booking_class = models.CharField(max_length=25, null=True, blank=True)
    date = models.DateField(auto_now_add=True)
    flight_route = models.CharField(max_length=255, null=True, blank=True)
    departure_city = models.CharField(max_length=255, null=True, blank=True)
    departure_airport = models.CharField(max_length=255, null=True, blank=True)
    arrival_city = models.CharField(max_length=255, null=True, blank=True)
    arrival_airport = models.CharField(max_length=255, null=True, blank=True)
    flight_route_time = models.TimeField(max_length=255, null=True, blank=True)
    departure_time = models.TimeField(max_length=255, null=True, blank=True)
    arrival_time = models.TimeField(max_length=255, null=True, blank=True)
    carrier = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.id}"

    class Meta:
        db_table = 'ticket'

